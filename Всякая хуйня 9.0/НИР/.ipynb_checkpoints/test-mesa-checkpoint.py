from mesa.discrete_space import CellAgent

class MoneyAgent(CellAgent):
    """An agent with fixed initial wealth.

    Each agent starts with 1 unit of wealth and can give 1 unit to other agents
    if they occupy the same cell.

    Attributes:
        wealth (int): The agent's current wealth (starts at 1)
    """

    def __init__(self, model, cell):
        """Create a new agent.

        Args:
            model (Model): The model instance that contains the agent
        """
        super().__init__(model)
        self.cell = cell
        self.wealth = 1

    def move(self):
        """Move the agent to a random neighboring cell."""
        self.cell = self.cell.neighborhood.select_random_cell()

    def give_money(self):
        """Give 1 unit of wealth to a random agent in the same cell."""
        cellmates = [a for a in self.cell.agents if a is not self]

        if cellmates:  # Only give money if there are other agents present
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

    def step(self):
        """Execute one step for the agent:
        1. Move to a neighboring cell
        2. If wealth > 0, maybe give money to another agent in the same cell
        """
        self.move()
        if self.wealth > 0:
            self.give_money()

"""
Boltzmann Wealth Model
=====================

A simple model of wealth distribution based on the Boltzmann-Gibbs distribution.
Agents move randomly on a grid, giving one unit of wealth to a random neighbor
when they occupy the same cell.
"""

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.discrete_space import OrthogonalMooreGrid
from mesa.examples.basic.boltzmann_wealth_model.agents import MoneyAgent


class BoltzmannWealth(Model):
    """A simple model of an economy where agents exchange currency at random.

    All agents begin with one unit of currency, and each time step agents can give
    a unit of currency to another agent in the same cell. Over time, this produces
    a highly skewed distribution of wealth.

    Attributes:
        num_agents (int): Number of agents in the model
        grid (MultiGrid): The space in which agents move
        running (bool): Whether the model should continue running
        datacollector (DataCollector): Collects and stores model data
    """

    def __init__(self, n=100, width=10, height=10, seed=None):
        """Initialize the model.

        Args:
            n (int, optional): Number of agents. Defaults to 100.
            width (int, optional): Grid width. Defaults to 10.
            height (int, optional): Grid height. Defaults to 10.
            seed (int, optional): Random seed. Defaults to None.
        """
        super().__init__(seed=seed)

        self.num_agents = n
        self.grid = OrthogonalMooreGrid((width, height), random=self.random)

        # Set up data collection
        self.datacollector = DataCollector(
            model_reporters={"Gini": self.compute_gini},
            agent_reporters={"Wealth": "wealth"},
        )
        MoneyAgent.create_agents(
            self,
            self.num_agents,
            self.random.choices(self.grid.all_cells.cells, k=self.num_agents),
        )

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.agents.shuffle_do("step")  # Activate all agents in random order
        self.datacollector.collect(self)  # Collect data

    def compute_gini(self):
        """Calculate the Gini coefficient for the model's current wealth distribution.

        The Gini coefficient is a measure of inequality in distributions.
        - A Gini of 0 represents complete equality, where all agents have equal wealth.
        - A Gini of 1 represents maximal inequality, where one agent has all wealth.
        """
        agent_wealths = [agent.wealth for agent in self.agents]
        x = sorted(agent_wealths)
        n = self.num_agents
        # Calculate using the standard formula for Gini coefficient
        b = sum(xi * (n - i) for i, xi in enumerate(x)) / (n * sum(x))
        return 1 + (1 / n) - 2 * b

import altair as alt

from mesa.examples.basic.boltzmann_wealth_model.model import BoltzmannWealth
from mesa.mesa_logging import INFO, log_to_stderr
from mesa.visualization import (
    SolaraViz,
    SpaceRenderer,
    make_plot_component,
)
from mesa.visualization.components import AgentPortrayalStyle

log_to_stderr(INFO)


def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color=agent.wealth
    )  # we are using a colormap to translate wealth to color


model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "n": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "width": 10,
    "height": 10,
}


def post_process(chart):
    """Post-process the Altair chart to add a colorbar legend."""
    chart = chart.encode(
        color=alt.Color(
            "color:N",
            scale=alt.Scale(scheme="viridis", domain=[0, 10]),
            legend=alt.Legend(
                title="Wealth",
                orient="right",
                type="gradient",
                gradientLength=200,
            ),
        ),
    )
    return chart


model = BoltzmannWealth(50, 10, 10)

# The SpaceRenderer is responsible for drawing the model's space and agents.
# It builds the visualization in layers, first drawing the grid structure,
# and then drawing the agents on top. It uses a specified backend
# (like "altair" or "matplotlib") for creating the plots.
renderer = SpaceRenderer(model, backend="altair")
# Can customize the grid appearance.
renderer.draw_structure(grid_color="black", grid_dash=[6, 2], grid_opacity=0.3)
renderer.draw_agents(agent_portrayal=agent_portrayal, cmap="viridis", vmin=0, vmax=10)

# The post_process function is used to modify the Altair chart after it has been created.
# It can be used to add legends, colorbars, or other visual elements.
renderer.post_process = post_process

# Creates a line plot component from the model's "Gini" datacollector.
GiniPlot = make_plot_component("Gini")

# The SolaraViz page combines the model, renderer, and components into a web interface.
# To run the visualization, save this code as app.py and run `solara run app.py`
page = SolaraViz(
    model,
    renderer,
    components=[GiniPlot],
    model_params=model_params,
    name="Boltzmann Wealth Model",
)
page  # noqa

