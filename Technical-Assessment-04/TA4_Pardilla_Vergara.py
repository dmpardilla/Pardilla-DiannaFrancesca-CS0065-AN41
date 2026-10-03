import os
import sys
import time
from typing import Dict, List, Any, Tuple

# TERMINAL UI & AESTHETICS (BUTTON STYLING + ALIGNED BORDERS)
class UI:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"

    # Inner width between the vertical pipes: | ... 74 chars ... |
    INNER_WIDTH = 74

    @classmethod
    def header(cls) -> None:
        cls.clear()
        w = cls.INNER_WIDTH
        
        top_border = f"{cls.CYAN}+{'-' * w}+{cls.RESET}"
        mid_border = f"{cls.CYAN}+{'-' * w}+{cls.RESET}"
        bot_border = f"{cls.CYAN}+{'-' * w}+{cls.RESET}"

        # Plain text strings for exact width calculation
        t1_plain = "INTELLIGENT SYSTEMS: REASONING & INFERENCE ENGINE"
        t2_plain = "CS0065 - Technical Assessment 4"
        l3_plain = "  Programmed by : Dianna Francesca M. Pardilla & Justin D. Vergara"
        l4_plain = "  Section       : CS0065 - AN41"

        # Centered titles
        t1_pad = (w - len(t1_plain)) // 2
        t1_formatted = " " * t1_pad + f"{cls.BOLD}{t1_plain}{cls.RESET}" + " " * (w - len(t1_plain) - t1_pad)

        t2_pad = (w - len(t2_plain)) // 2
        t2_formatted = " " * t2_pad + f"{cls.DIM}{t2_plain}{cls.RESET}" + " " * (w - len(t2_plain) - t2_pad)

        # Left-aligned info lines with exact trailing space padding
        l3_formatted = f"  Programmed by : {cls.BOLD}Dianna Francesca M. Pardilla & Justin D. Vergara{cls.RESET}" + " " * (w - len(l3_plain))
        l4_formatted = f"  Section       : {cls.YELLOW}CS0065 - AN41{cls.RESET}" + " " * (w - len(l4_plain))

        # Render Header Box
        print(top_border)
        print(f"{cls.CYAN}|{cls.RESET}{t1_formatted}{cls.CYAN}|{cls.RESET}")
        print(f"{cls.CYAN}|{cls.RESET}{t2_formatted}{cls.CYAN}|{cls.RESET}")
        print(mid_border)
        print(f"{cls.CYAN}|{cls.RESET}{l3_formatted}{cls.CYAN}|{cls.RESET}")
        print(f"{cls.CYAN}|{cls.RESET}{l4_formatted}{cls.CYAN}|{cls.RESET}")
        print(bot_border)

    @classmethod
    def section(cls, title: str, part_num: str) -> None:
        """Displays section headers with a stylized < BUTTON > banner."""
        tag_btn = f"{cls.MAGENTA}< {cls.BOLD}{part_num}{cls.RESET}{cls.MAGENTA} >{cls.RESET}"
        title_btn = f"{cls.CYAN}< {cls.BOLD}{title.upper()}{cls.RESET}{cls.CYAN} >{cls.RESET}"
        print(f"\n{tag_btn} ─── {title_btn}\n")

    @classmethod
    def button(cls, key: str, label: str) -> str:
        """Returns a formatted button string for menu choices."""
        badge = f"{cls.CYAN}< {cls.BOLD}{key}{cls.RESET}{cls.CYAN} >{cls.RESET}"
        return f"  {badge} {label}"

    @classmethod
    def pause(cls) -> None:
        print(f"\n{cls.DIM}Press Enter to return to main menu...{cls.RESET}", end="")
        input()

    @classmethod
    def clear(cls) -> None:
        os.system("cls" if os.name == "nt" else "clear")

# PART 1: KNOWLEDGE REPRESENTATION (KR) SETUP
knowledge_base: Dict[str, Any] = {
    # Category 1: Thermals & Environment
    "core_temperature_celsius": 86,
    "ambient_humidity_percent": 74,
    
    # Category 2: Resource Utilization & Power
    "cpu_load_percent": 96,
    "cooling_pump_active": False,
    "battery_charge_percent": 15,
    
    # Category 3: System Health & Hardware Flags
    "disk_io_errors": True,
    "network_latency_ms": 350
}


def display_knowledge_base() -> None:
    UI.header()
    UI.section("Knowledge Representation (Working Memory)", "PART 1")
    
    print(f"  {UI.BOLD}{'Telemetry Parameter':<32} │ {'State / Value'}{UI.RESET}")
    print("  " + "─" * 56)
    
    for key, value in knowledge_base.items():
        label = key.replace("_", " ").title()
        if isinstance(value, bool):
            val_display = f"{UI.RED}< CRITICAL: True >{UI.RESET}" if value else f"{UI.DIM}< NORMAL: False >{UI.RESET}"
        elif isinstance(value, (int, float)) and ("temp" in key or "load" in key):
            val_display = f"{UI.YELLOW}< {value} >{UI.RESET}"
        else:
            val_display = f"{UI.GREEN}< {value} >{UI.RESET}"
        
        print(f"  • {label:<30} │ {val_display}")
    
    UI.pause()

# PART 2: RULE-BASED REASONING (RBR)
def rule_thermal_critical(facts: Dict[str, Any]) -> str | None:
    if facts.get("core_temperature_celsius", 0) > 80:
        return "Thermal overload (>80°C) -> Trigger immediate CPU clock down-throttling."
    return None

def rule_cooling_failure(facts: Dict[str, Any]) -> str | None:
    if facts.get("core_temperature_celsius", 0) > 75 and not facts.get("cooling_pump_active", True):
        return "Cooling pump offline under high load -> Force auxiliary high-RPM fan bypass."
    return None

def rule_battery_preservation(facts: Dict[str, Any]) -> str | None:
    if facts.get("battery_charge_percent", 100) < 20:
        return "Reserve power depleted (<20%) -> Terminate secondary GPU threads and background tasks."
    return None

def rule_disk_anomaly(facts: Dict[str, Any]) -> str | None:
    if facts.get("disk_io_errors", False):
        return "I/O integrity flags asserted -> Mount main file-system partition as read-only."
    return None


class InferenceEngine:
    def __init__(self, rule_list: List[Any]):
        self.rules = rule_list

    def run(self, facts: Dict[str, Any]) -> List[Tuple[str, str]]:
        deductions = []
        for i, r in enumerate(self.rules, start=1):
            result = r(facts)
            if result:
                deductions.append((f"RBR-{i:02d}", result))
        return deductions


def run_rule_based_reasoning() -> None:
    UI.header()
    UI.section("Rule-Based Reasoning (Inference Cycle)", "PART 2")
    
    engine = InferenceEngine([
        rule_thermal_critical,
        rule_cooling_failure,
        rule_battery_preservation,
        rule_disk_anomaly
    ])
    
    print(f"  {UI.DIM}[*] Evaluating working memory across defined production rules...{UI.RESET}")
    time.sleep(0.3)
    actions = engine.run(knowledge_base)
    
    print(f"\n  {UI.BOLD}Inferred Prescriptive Actions ({len(actions)} matched):{UI.RESET}\n")
    for rule_id, act in actions:
        btn_tag = f"{UI.YELLOW}< {rule_id} >{UI.RESET}"
        print(f"   {btn_tag} {act}")
        
    UI.pause()

# PART 3: CASE-BASED REASONING (CBR) - 4R CYCLE
case_base: List[Dict[str, Any]] = [
    {
        "id": "CASE-101",
        "problem": {"overheating": True, "fan_spinning": False, "loud_buzzing": False, "blue_screen": False},
        "solution": "Clean heatsink fins and replace blocked auxiliary fan motor."
    },
    {
        "id": "CASE-102",
        "problem": {"overheating": True, "fan_spinning": True, "loud_buzzing": True, "blue_screen": False},
        "solution": "Inspect fan blades for physical friction; lubricate bearing housing."
    },
    {
        "id": "CASE-103",
        "problem": {"overheating": False, "fan_spinning": True, "loud_buzzing": False, "blue_screen": True},
        "solution": "Run memory diagnostic tool (memtest86) to detect degraded RAM modules."
    },
    {
        "id": "CASE-104",
        "problem": {"overheating": True, "fan_spinning": False, "loud_buzzing": True, "blue_screen": True},
        "solution": "Power supply unit (PSU) rail short-circuit; perform full board inspection."
    }
]


def compute_similarity(stored_problem: Dict[str, bool], incoming_problem: Dict[str, bool]) -> float:
    keys = set(stored_problem.keys()) & set(incoming_problem.keys())
    if not keys:
        return 0.0
    matches = sum(1 for k in keys if stored_problem[k] == incoming_problem[k])
    return (matches / len(keys)) * 100.0


def retrieve(incoming: Dict[str, bool]) -> Tuple[Dict[str, Any], float]:
    best_match = None
    highest_score = -1.0
    for case in case_base:
        score = compute_similarity(case["problem"], incoming)
        if score > highest_score:
            highest_score = score
            best_match = case
    return best_match, highest_score


def run_case_based_reasoning() -> None:
    UI.header()
    UI.section("Case-Based Reasoning (4R Cycle)", "PART 3")
    
    incoming_case = {
        "overheating": True,
        "fan_spinning": False,
        "loud_buzzing": False,
        "blue_screen": True
    }
    
    print(f"  {UI.BOLD}Incoming Problem Vector:{UI.RESET}")
    for k, v in incoming_case.items():
        print(f"    • {k:<15}: {v}")
    
    # Step 1: RETRIEVE
    print(f"\n  {UI.CYAN}< 1. RETRIEVE >{UI.RESET} Searching case library for closest pattern...")
    time.sleep(0.3)
    matched_case, score = retrieve(incoming_case)
    print(f"  -> Best Match : {UI.BOLD}< {matched_case['id']} >{UI.RESET} (Similarity: {UI.GREEN}{score:.1f}%{UI.RESET})")
    
    # Step 2: REUSE
    print(f"\n  {UI.CYAN}< 2. REUSE >{UI.RESET} Retrieved Solution:")
    reused_solution = matched_case["solution"]
    print(f"  -> \"{reused_solution}\"")
    
    # Step 3: REVISE
    print(f"\n  {UI.CYAN}< 3. REVISE >{UI.RESET} Adjusting solution for unique symptom traits:")
    print("  -> Enter adjusted solution (press Enter to keep default): ")
    user_adj = input("     > ").strip()
    revised_solution = user_adj if user_adj else f"{reused_solution} + [Addendum: Verify PSU voltage output]."
    print(f"  -> Final Solution: {UI.YELLOW}{revised_solution}{UI.RESET}")
    
    # Step 4: RETAIN
    print(f"\n  {UI.CYAN}< 4. RETAIN >{UI.RESET} Archiving resolved case into memory base...")
    new_id = f"CASE-{len(case_base) + 101}"
    learned_case = {
        "id": new_id,
        "problem": incoming_case,
        "solution": revised_solution
    }
    case_base.append(learned_case)
    print(f"  -> Case registered as {UI.BOLD}< {new_id} >{UI.RESET}.")
    print(f"  -> Total stored cases: {UI.GREEN}{len(case_base)}{UI.RESET}")
    
    UI.pause()


def view_all_cases() -> None:
    UI.header()
    UI.section("Archived Case Base Repository", "CASE VIEWER")
    for case in case_base:
        print(f"  {UI.MAGENTA}< {case['id']} >{UI.RESET}")
        print(f"    Features : {case['problem']}")
        print(f"    Solution : {UI.GREEN}{case['solution']}{UI.RESET}\n")
    UI.pause()

# MAIN MENU LOOP
def main_menu() -> None:
    while True:
        UI.header()
        print("\n  Select a module to execute:\n")
        print(UI.button("1", "View Knowledge Base (Part 1 - KR)"))
        print(UI.button("2", "Run Rule-Based Reasoning Engine (Part 2 - RBR)"))
        print(UI.button("3", "Execute Case-Based Reasoning Pipeline (Part 3 - CBR 4R)"))
        print(UI.button("4", "View All Retained Cases in Memory"))
        print(UI.button("5", "Exit System"))
        print("\n  " + "─" * 50)
        
        choice = input(f"  {UI.CYAN}< INPUT >{UI.RESET} Enter Choice [1-5]: ").strip()
        
        if choice == "1":
            display_knowledge_base()
        elif choice == "2":
            run_rule_based_reasoning()
        elif choice == "3":
            run_case_based_reasoning()
        elif choice == "4":
            view_all_cases()
        elif choice == "5":
            UI.header()
            print(f"\n  {UI.GREEN}< OK > System session closed. Thank you!{UI.RESET}\n")
            sys.exit(0)
        else:
            print(f"\n  {UI.RED}< ERROR > Invalid choice! Please enter a number from 1 to 5.{UI.RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()