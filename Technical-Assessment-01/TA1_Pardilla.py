import random
import agentpy as ap
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# -------- 1. Console Inputs --------
num_agents = int(input("Enter number of agents: "))
grid_size = int(input("Enter grid size (e.g., 10 for 10x10): "))
num_steps = int(input("Enter number of steps: "))


# -------- 2. Agent Definition -----------
class PathTrackingWalker(ap.Agent):

  def setup(self):
    self.trajectory = []

  def step(self):
    # Rule change: Weighted drift (40% right, 20% left, up, down)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    weights = [0.40, 0.20, 0.20, 0.20]
    direction = random.choices(moves, weights=weights, k=1)[0]

    x, y = self.position
    new_x = max(0, min(self.model.p.grid_size[0] - 1, x + direction[0]))
    new_y = max(0, min(self.model.p.grid_size[1] - 1, y + direction[1]))

    self.position = (new_x, new_y)
    self.trajectory.append(self.position)


# -------- 3. Model Definition -----------
class RandomWalkModel(ap.Model):

  def setup(self):
    self.agents = ap.AgentList(self, self.p.agents, PathTrackingWalker)

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
    print("\n" + "=" * 45)
    print("--- SIMULATION COMPLETE: FINAL POSITIONS ---")
    print("=" * 45)
    for i, agent in enumerate(self.agents, 1):
      print(
          f"Agent {i:02d} | Final Position: {agent.position} | Total Points:"
          f" {len(agent.trajectory)}"
      )
    print("=" * 45 + "\n")


# -------- 4. Model Setup -----------
parameters = {
    "agents": num_agents,
    "grid_size": (grid_size, grid_size),
    "steps": num_steps,
}

model = RandomWalkModel(parameters)
model.setup()

# -------- 5. Interactive Visualizer -----------
fig, ax = plt.subplots(figsize=(6, 6))


def update(frame):
  if frame > 0:
    model.step()

  ax.clear()
  ax.set_xlim(-0.5, model.p.grid_size[0] - 0.5)
  ax.set_ylim(-0.5, model.p.grid_size[1] - 0.5)
  ax.set_xticks(range(model.p.grid_size[0]))
  ax.set_yticks(range(model.p.grid_size[1]))
  ax.grid(True, linestyle="--", alpha=0.5)
  ax.set_title(f"Step {frame}/{model.p.steps} - Path Tracing")

  # Draw movement trails
  for agent in model.agents:
    xs, ys = zip(*agent.trajectory)
    ax.plot(xs, ys, alpha=0.5, linewidth=1.5)

  # Draw current agent positions
  cx = [agent.position[0] for agent in model.agents]
  cy = [agent.position[1] for agent in model.agents]
  scat = ax.scatter(cx, cy, s=120, c="crimson", edgecolors="black", zorder=3)

  if frame == model.p.steps:
    model.end()

  return (scat,)


ani = animation.FuncAnimation(
    fig, update, frames=model.p.steps + 1, repeat=False, interval=200
)

plt.tight_layout()
plt.show()