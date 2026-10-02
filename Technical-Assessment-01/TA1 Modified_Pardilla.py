import random
import agentpy as ap
import matplotlib.animation as animation
import matplotlib.pyplot as plt

APP_TITLE = "GridDrift: Multi-Agent Random Walk Simulation"

# < CONSOLE BANNER & HEADER >
print(f" {APP_TITLE} ")
print(" CS0065 (Intelligent Systems) | Section: AN41")
print(" Programmed by: Dianna Francesca M. Pardilla")
print(" Date: October 2, 2026")
print("~" * 60 + "\n")

# 1. < USER INPUTS >
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))

# 2. < AGENT DEFINITION (LAB TASKS) >
class CustomWalker(ap.Agent):

  def setup(self):
    self.trajectory = []

  def step(self):
    # Rule change: Weighted drift (40% right, 20% left, up, down)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    weights = [0.40, 0.20, 0.20, 0.20]
    direction = random.choices(moves, weights=weights, k=1)[0]

    x, y = self.position

    # Keep agents inside grid limits
    bounded_x = max(
        0, min(self.model.p.grid_size[0] - 1, x + direction[0])
    )  #[cite: 1]
    bounded_y = max(
        0, min(self.model.p.grid_size[1] - 1, y + direction[1])
    )  #[cite: 1]

    self.position = (bounded_x, bounded_y)
    self.trajectory.append(self.position)

# 3. < MODEL DEFINITION >
class RandomWalkModel(ap.Model):

  def setup(self):
    self.agents = ap.AgentList(self, self.p.agents, CustomWalker)

    for agent in self.agents:
      init_pos = (
          random.randint(0, self.p.grid_size[0] - 1),
          random.randint(0, self.p.grid_size[1] - 1),
      )
      agent.position = init_pos
      agent.trajectory.append(init_pos)

    self.grid = ap.Grid(self, self.p.grid_size, torus=False)
    self.grid.add_agents(self.agents)

  def step(self):
    self.agents.step()

  def end(self):
    print("\n" + "~" * 60)
    print("                 FINAL POSITIONS SUMMARY                     ")
    print(" Programmed by: Dianna Francesca M. Pardilla | AN41          ")
    print("~" * 60 + "\n")
    for i, agent in enumerate(self.agents, 1):
      start_coord = agent.trajectory[0]
      final_coord = agent.position
      print(
          f"Agent {i:02d} | Start: {start_coord} | Final: {final_coord} | Total"
          f" Steps: {len(agent.trajectory) - 1}"
      )
    print("=" * 60 + "\n")

# 4. < EXECUTION & ANIMATION >
parameters = {
    "agents": num_agents,
    "grid_size": (grid_size, grid_size),
    "steps": num_steps,
}

model = RandomWalkModel(parameters)
model.setup()

fig, ax = plt.subplots(figsize=(7, 7))


def update(frame):
  if frame > 0:
    model.step()

  ax.clear()
  ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
  ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)
  ax.set_xticks(range(model.p.grid_size[0]))
  ax.set_yticks(range(model.p.grid_size[1]))
  ax.grid(True, linestyle="--", alpha=0.5)

  # Clean title header on the plot window
  ax.set_title(
      f"{APP_TITLE}\n"
      "Programmed by: Dianna Francesca M. Pardilla | CS0065 - AN41\n"
      f"Step: {frame}/{model.p.steps} | Date: October 2, 2026",
      fontsize=10,
      pad=10,
  )

  # Draw movement trails
  for agent in model.agents:
    xs, ys = zip(*agent.trajectory)
    ax.plot(xs, ys, alpha=0.45, linewidth=1.5)

  # Draw current positions
  cx = [agent.position[0] for agent in model.agents]
  cy = [agent.position[1] for agent in model.agents]
  scat = ax.scatter(
      cx, cy, s=120, c="crimson", edgecolors="black", zorder=3, label="Agents"
  )

  if frame == model.p.steps:
    model.end()

  return (scat,)


ani = animation.FuncAnimation(
    fig, update, frames=model.p.steps + 1, repeat=False, interval=200
)

plt.tight_layout()
plt.show()