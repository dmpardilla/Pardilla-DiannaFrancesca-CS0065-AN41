from dataclasses import dataclass
from enum import Enum
import random
import time

# CLI THEME PALETTE & VISUAL ASSETS
class TerminalPalette:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    MAGENTA = "\033[95m"
    RED     = "\033[91m"
    BLUE    = "\033[94m"

class RoomStatus(str, Enum):
    DIRTY = "Dirty"
    CLEAN = "Clean"

# TASK 1: ENVIRONMENT SETUP & ABSTRACTION
class DualChamberEnvironment:
    """Manages the two-room spatial state dictionary and mutation hooks."""
    
    def __init__(self, room_a_state: str = "Clean", room_b_state: str = "Clean"):
        # Task 1: Initialize two rooms using a Python dictionary
        self._chambers: dict[str, RoomStatus] = {
            'A': RoomStatus.DIRTY if room_a_state.strip().capitalize() == "Dirty" else RoomStatus.CLEAN,
            'B': RoomStatus.DIRTY if room_b_state.strip().capitalize() == "Dirty" else RoomStatus.CLEAN
        }

    @property
    def chambers(self) -> dict[str, str]:
        return {room: status.value for room, status in self._chambers.items()}

    def is_dirty(self, room: str) -> bool:
        """Task 1: Sensor function to verify chamber dirt presence."""
        return self._chambers.get(room) == RoomStatus.DIRTY

    def clean_room(self, room: str) -> None:
        """Task 1: Actuator hook to sanitize the designated room."""
        if room in self._chambers:
            self._chambers[room] = RoomStatus.CLEAN

# TASK 2: RULE-BASED REFLEX AGENT
class ReflexVacuumAgent:
    """Production-rule reflex agent executing condition-action directives."""

    def __init__(self, origin: str = 'A'):
        self.location: str = origin.upper()

    def move(self) -> None:
        """Task 2: Navigates across the binary topological room layout."""
        self.location = 'B' if self.location == 'A' else 'A'

    def perceive_and_act(self, env: DualChamberEnvironment) -> tuple[str, str]:
        """
        Task 2: Evaluate sensory percept and trigger conditional action.
        - Rule 1: If current chamber is Dirty -> Purge contaminant.
        - Rule 2: If current chamber is Clean -> Relocate to counter-chamber.
        """
        origin = self.location
        
        # Rule 1
        if env.is_dirty(origin):
            env.clean_room(origin)
            return ("RULE_1", f"Sanitized dirty chamber [{origin}]")
        
        # Rule 2
        self.move()
        return ("RULE_2", f"Relocated chamber: [{origin}] -> [{self.location}]")

# TASK 3: SIMULATION RUNNER & HUD PRINTER
def print_telemetry_card(step_num: int, origin_loc: str, rule_fired: str, action_desc: str, room_states: dict[str, str]) -> None:
    """Formats and prints an ASCII telemetry HUD card for each execution step."""
    p = TerminalPalette
    
    # State color tags
    def badge(status: str) -> str:
        return f"{p.RED}DIRTY{p.RESET}" if status == "Dirty" else f"{p.GREEN}CLEAN{p.RESET}"

    border = f"{p.DIM}+---------------------------------------------------------------+{p.RESET}"
    rule_tag = f"{p.YELLOW}[CLEAN]{p.RESET}" if rule_fired == "RULE_1" else f"{p.CYAN}[RELOCATE]{p.RESET}"
    
    print(border)
    print(f"|  {p.BOLD}CYCLE {step_num:02d}{p.RESET}  ::  {rule_tag}  {action_desc:<37} |")
    print(f"|  {p.DIM}Percept Position :{p.RESET} Chamber [{p.MAGENTA}{origin_loc}{p.RESET}]                             |")
    print(f"|  {p.DIM}Chamber Telemetry:{p.RESET} Room A -> {badge(room_states['A']):<18} Room B -> {badge(room_states['B']):<18} |")
    print(border)


def run_standard_simulation() -> None:
    p = TerminalPalette
    while True:
        print(f"\n{p.CYAN}┌───────────────────────────────────────────────────────────────┐{p.RESET}")
        print(f"{p.CYAN}│{p.RESET}       {p.BOLD}TASKS 1, 2 & 3: 2-ROOM AGENT SIMULATION BENCHMARK{p.RESET}       {p.CYAN}│{p.RESET}")
        print(f"{p.CYAN}└───────────────────────────────────────────────────────────────┘{p.RESET}\n")

        # Task 1 & 3: Interactive environment parameter setup
        raw_a = input(f"{p.DIM}» Initial State for Chamber A (Clean/Dirty): {p.RESET}").strip()
        raw_b = input(f"{p.DIM}» Initial State for Chamber B (Clean/Dirty): {p.RESET}").strip()
        raw_loc = input(f"{p.DIM}» Initial Agent Deployment Chamber (A/B): {p.RESET}").strip().upper()
        start_loc = raw_loc if raw_loc in ['A', 'B'] else 'A'

        env = DualChamberEnvironment(raw_a, raw_b)
        agent = ReflexVacuumAgent(start_loc)

        try:
            steps = int(input(f"{p.DIM}» Execution Step Limit: {p.RESET}"))
        except ValueError:
            steps = 4
            print(f"{p.YELLOW}! Invalid integer; defaulting to 4 cycles.{p.RESET}")

        print(f"\n{p.BOLD}--- EXECUTION TRACE INITIATED ---{p.RESET}\n")
        time.sleep(0.2)

        # Task 3: Execution loop
        for step in range(1, steps + 1):
            prior_loc = agent.location
            rule_id, telemetry = agent.perceive_and_act(env)
            print_telemetry_card(step, prior_loc, rule_id, telemetry, env.chambers)

        # Interactive loop control
        retry = input(f"\n{p.MAGENTA}» Rerun 2-Chamber simulation? (y/N): {p.RESET}").strip().lower()
        if retry != 'y':
            break

# BONUS TASK: 3-CHAMBER VISUAL MATRIX & GRID ENGINE
class MultiChamberEnvironment:
    """Dynamic spatial matrix with variable capacity (Rooms A, B, and C)."""
    
    def __init__(self, states: dict[str, str]):
        self.rooms = {k: RoomStatus.DIRTY if v.strip().capitalize() == "Dirty" else RoomStatus.CLEAN for k, v in states.items()}

    def is_dirty(self, room: str) -> bool:
        return self.rooms.get(room) == RoomStatus.DIRTY

    def clean(self, room: str) -> None:
        self.rooms[room] = RoomStatus.CLEAN

    def dirty_nodes(self) -> list[str]:
        return [node for node, state in self.rooms.items() if state == RoomStatus.DIRTY]


class StochasticMatrixAgent:
    """Agent that handles dynamic chambers and targets dirty rooms randomly."""

    def __init__(self, initial_node: str = 'A'):
        self.node = initial_node.upper()

    def cycle(self, env: MultiChamberEnvironment) -> str:
        curr = self.node
        if env.is_dirty(curr):
            env.clean(curr)
            return f"Purged contaminant at Room {curr}"

        dirty_set = [r for r in env.dirty_nodes() if r != curr]
        if dirty_set:
            self.node = random.choice(dirty_set)
            return f"Vector Lock: Shifted to Dirty Node [{self.node}]"
        
        adjacent = [r for r in env.rooms.keys() if r != curr]
        self.node = random.choice(adjacent)
        return f"Patrol Vector: Sweeping Clean Node [{self.node}]"


def render_isometric_grid(room_dict: dict[str, RoomStatus], current_loc: str) -> None:
    """Draws a clean, styled spatial grid showing the agent's live coordinates."""
    p = TerminalPalette
    
    def render_pod(chamber_id: str) -> tuple[str, str]:
        is_here = (current_loc == chamber_id)
        is_polluted = (room_dict[chamber_id] == RoomStatus.DIRTY)
        
        status_txt = f"{p.RED}DIRTY{p.RESET}" if is_polluted else f"{p.GREEN}CLEAN{p.RESET}"
        cursor_txt = f"{p.YELLOW}[AGENT]{p.RESET}" if is_here else "         "
        
        line_status = f"│ Status : {status_txt:<15} "
        line_cursor = f"│ Pos    : {cursor_txt:<18} "
        return line_status, line_cursor

    box_top    = "+-------------------------+-------------------------+-------------------------+"
    box_header = f"| Chamber A               | Chamber B               | Chamber C               |"
    box_div    = "+-------------------------+-------------------------+-------------------------+"
    box_bottom = "+-------------------------+-------------------------+-------------------------+"

    s_a, c_a = render_pod('A')
    s_b, c_b = render_pod('B')
    s_c, c_c = render_pod('C')

    print(f"{p.DIM}{box_top}{p.RESET}")
    print(f"{p.BOLD}{box_header}{p.RESET}")
    print(f"{p.DIM}{box_div}{p.RESET}")
    print(f"{s_a}{s_b}{s_c}│")
    print(f"{c_a}{c_b}{c_c}│")
    print(f"{p.DIM}{box_bottom}{p.RESET}")


def run_bonus_simulation() -> None:
    p = TerminalPalette
    while True:
        print(f"\n{p.MAGENTA}┌───────────────────────────────────────────────────────────────┐{p.RESET}")
        print(f"{p.MAGENTA}│{p.RESET}         {p.BOLD}BONUS: 3-CHAMBER VISUAL MATRIX SIMULATION{p.RESET}             {p.MAGENTA}│{p.RESET}")
        print(f"{p.MAGENTA}└───────────────────────────────────────────────────────────────┘{p.RESET}\n")

        states = {
            'A': input(f"{p.DIM}» Chamber A State (Clean/Dirty): {p.RESET}"),
            'B': input(f"{p.DIM}» Chamber B State (Clean/Dirty): {p.RESET}"),
            'C': input(f"{p.DIM}» Chamber C State (Clean/Dirty): {p.RESET}")
        }
        start = input(f"{p.DIM}» Deploy Agent to Chamber (A/B/C): {p.RESET}").strip().upper()
        start_node = start if start in ['A', 'B', 'C'] else 'A'

        try:
            cycles = int(input(f"{p.DIM}» Step Limit: {p.RESET}"))
        except ValueError:
            cycles = 4

        env = MultiChamberEnvironment(states)
        agent = StochasticMatrixAgent(start_node)

        print(f"\n{p.BOLD}T-0 MATRIX INITIALIZATION:{p.RESET}")
        render_isometric_grid(env.rooms, agent.node)

        for c in range(1, cycles + 1):
            act = agent.cycle(env)
            print(f"\n{p.CYAN}STEP {c:02d} ACTUATOR:{p.RESET} {act}")
            render_isometric_grid(env.rooms, agent.node)

        retry = input(f"\n{p.MAGENTA}» Rerun 3-Chamber simulation? (y/N): {p.RESET}").strip().lower()
        if retry != 'y':
            break

# MAIN COMMAND INTERFACE
def main():
    p = TerminalPalette
    while True:
        print(f"\n{p.CYAN}╔═══════════════════════════════════════════════════════════════╗{p.RESET}")
        print(f"{p.CYAN}║{p.RESET}     {p.BOLD}CS0065: INTELLIGENT SYSTEMS - REFLEX AGENT BENCHMARK{p.RESET}      {p.CYAN}║{p.RESET}")
        print(f"{p.CYAN}╚═══════════════════════════════════════════════════════════════╝{p.RESET}")
        print(f" {p.CYAN}[1]{p.RESET} Execute Tasks 1, 2, & 3 (2-Chamber Production Model)")
        print(f" {p.CYAN}[2]{p.RESET} Execute Bonus Grid Matrix (3-Chamber Stochastic Model)")
        print(f" {p.CYAN}[3]{p.RESET} Terminate Session")
        
        selection = input(f"\n{p.BOLD}» Command Interface Index (1/2/3): {p.RESET}").strip()
        
        if selection == '1':
            run_standard_simulation()
        elif selection == '2':
            run_bonus_simulation()
        elif selection == '3':
            print(f"\n{p.DIM}Session closed cleanly.{p.RESET}\n")
            break
        else:
            print(f"{p.RED}! Unknown command index.{p.RESET}")


if __name__ == "__main__":
    main()