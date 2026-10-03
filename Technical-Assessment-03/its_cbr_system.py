from dataclasses import dataclass
from typing import List, Tuple, Optional
import time

# ANSI PALETTE & UI STYLING ENGINE
class Style:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    
    # Soft Pastel Accents
    CYAN    = "\033[38;2;110;207;246m"
    LILAC   = "\033[38;2;199;146;234m"
    MINT    = "\033[38;2;137;221;110m"
    CORAL   = "\033[38;2;240;113;120m"
    GOLD    = "\033[38;2;255;203;107m"
    SLATE   = "\033[38;2;120;144;156m"
    WHITE   = "\033[38;2;238;255;255m"

def draw_header(title: str, subtitle: str, programmers: List[str], section: str) -> None:
    width = 72
    print(f"\n{Style.LILAC}╭{'─' * (width - 2)}╮{Style.RESET}")
    print(f"{Style.LILAC}│{Style.BOLD}{Style.WHITE} {title.center(width - 4)} {Style.RESET}{Style.LILAC}│{Style.RESET}")
    print(f"{Style.LILAC}│{Style.DIM}{Style.CYAN} {subtitle.center(width - 4)} {Style.RESET}{Style.LILAC}│{Style.RESET}")
    print(f"{Style.LILAC}├{'─' * (width - 2)}┤{Style.RESET}")
    
    prog_line = f"Programmed by: {', '.join(programmers)}"
    sec_line = f"Course & Section: {section}"
    print(f"{Style.LILAC}│{Style.SLATE} {prog_line.center(width - 4)} {Style.RESET}{Style.LILAC}│{Style.RESET}")
    print(f"{Style.LILAC}│{Style.SLATE} {sec_line.center(width - 4)} {Style.RESET}{Style.LILAC}│{Style.RESET}")
    print(f"{Style.LILAC}╰{'─' * (width - 2)}╯{Style.RESET}")

def draw_section(step_num: int, name: str, badge: str = "") -> None:
    badge_str = f" {Style.DIM}[{badge}]{Style.RESET}" if badge else ""
    print(f"\n{Style.BOLD}{Style.GOLD}▸ STEP {step_num}:{Style.RESET} {Style.BOLD}{Style.WHITE}{name}{Style.RESET}{badge_str}")
    print(f"{Style.SLATE}  {'┄' * 64}{Style.RESET}")

def render_meter(score: float, width: int = 18) -> str:
    filled = int(round(score * width))
    bar = "█" * filled + "░" * (width - filled)
    return f"{Style.MINT}{bar}{Style.RESET} {Style.BOLD}{score * 100:>5.1f}%{Style.RESET}"

# DOMAIN MODELS (Data Structures)
@dataclass
class ProblemState:
    topic: str
    error_type: str
    proficiency_level: str
    error_frequency: int

@dataclass
class RemedialIntervention:
    intervention: str
    recommended_practice: str
    difficulty_adjustment: str

@dataclass
class TutoringCase:
    case_id: str
    problem: ProblemState
    solution: RemedialIntervention

# 1. INITIAL CASE BASE
case_base: List[TutoringCase] = [
    TutoringCase(
        case_id="CASE-001",
        problem=ProblemState("Algebra", "Sign Error", "Beginner", 4),
        solution=RemedialIntervention(
            "Review integer sign rules with interactive number-line drills.",
            "5 foundational integer arithmetic exercises",
            "Decrease difficulty"
        )
    ),
    TutoringCase(
        case_id="CASE-002",
        problem=ProblemState("Algebra", "Formula Misuse", "Intermediate", 3),
        solution=RemedialIntervention(
            "Step-by-step formula breakdown focusing on variable substitution.",
            "3 guided formula substitution problems",
            "Maintain current difficulty"
        )
    ),
    TutoringCase(
        case_id="CASE-003",
        problem=ProblemState("Calculus", "Chain Rule Omission", "Advanced", 2),
        solution=RemedialIntervention(
            "Visual breakdown of nested functions and outer/inner derivative scaffolding.",
            "4 multi-step chain rule problems",
            "Maintain current difficulty"
        )
    ),
    TutoringCase(
        case_id="CASE-004",
        problem=ProblemState("Geometry", "Unit Mismatch", "Beginner", 5),
        solution=RemedialIntervention(
            "Unit conversion refresher focusing on metric dimension alignment.",
            "6 dimensional analysis drills",
            "Decrease difficulty"
        )
    ),
    TutoringCase(
        case_id="CASE-005",
        problem=ProblemState("Algebra", "Order of Operations", "Intermediate", 2),
        solution=RemedialIntervention(
            "PEMDAS sequence reinforcement using color-coded grouping brackets.",
            "4 precedence-focused evaluations",
            "Maintain current difficulty"
        )
    ),
]

# 2. SIMILARITY ASSESSMENT (Retrieve Stage)
def calculate_similarity(p1: ProblemState, p2: ProblemState) -> Tuple[float, dict]:
    weights = {"topic": 0.30, "error": 0.40, "proficiency": 0.15, "frequency": 0.15}
    
    s_topic = 1.0 if p1.topic.lower() == p2.topic.lower() else 0.0
    s_error = 1.0 if p1.error_type.lower() == p2.error_type.lower() else 0.0
    s_prof  = 1.0 if p1.proficiency_level.lower() == p2.proficiency_level.lower() else 0.0
    
    freq_delta = abs(p1.error_frequency - p2.error_frequency)
    s_freq  = max(0.0, 1.0 - (freq_delta / 5.0))
    
    total = (
        weights["topic"] * s_topic +
        weights["error"] * s_error +
        weights["proficiency"] * s_prof +
        weights["frequency"] * s_freq
    )
    
    breakdown = {
        "Topic Match": s_topic,
        "Error Match": s_error,
        "Level Match": s_prof,
        "Freq Proximity": round(s_freq, 2)
    }
    return round(total, 4), breakdown

def retrieve_best_case(new_problem: ProblemState) -> Tuple[TutoringCase, float, dict]:
    best_case: Optional[TutoringCase] = None
    best_score = -1.0
    best_breakdown = {}

    for case in case_base:
        score, breakdown = calculate_similarity(new_problem, case.problem)
        if score > best_score:
            best_score = score
            best_case = case
            best_breakdown = breakdown

    return best_case, best_score, best_breakdown

# 3. SOLUTION ADAPTATION (Reuse & Revise Stages)
def adapt_solution(retrieved_case: TutoringCase, new_prob: ProblemState) -> RemedialIntervention:
    base = retrieved_case.solution
    adapted_action = base.intervention
    adapted_practice = base.recommended_practice
    adapted_diff = base.difficulty_adjustment

    # Rule 1: High repeated error threshold (>= 4 repeats)
    if new_prob.error_frequency >= 4:
        adapted_diff = "Decrease difficulty (Remedial Mode Activated)"
        adapted_practice += " + 2 scaffolded verification drills"
    elif new_prob.error_frequency <= 1 and new_prob.proficiency_level.lower() == "advanced":
        adapted_diff = "Increase difficulty (Accelerated Track)"

    # Rule 2: Cross-topic domain adjustment
    if new_prob.topic.lower() != retrieved_case.problem.topic.lower():
        adapted_action += f" [Adapted from {retrieved_case.problem.topic} to {new_prob.topic}]"

    return RemedialIntervention(
        intervention=adapted_action,
        recommended_practice=adapted_practice,
        difficulty_adjustment=adapted_diff
    )

# 4. KNOWLEDGE RETENTION (Retain Stage)
def retain_case(new_problem: ProblemState, final_solution: RemedialIntervention) -> str:
    new_id = f"CASE-{len(case_base) + 1:03d}"
    learned_case = TutoringCase(
        case_id=new_id,
        problem=new_problem,
        solution=final_solution
    )
    case_base.append(learned_case)
    return new_id

# 5. EXECUTION PIPELINE
def run_its_cbr_pipeline(target_problem: ProblemState) -> None:
    # Step 1: Input Diagnosis
    draw_section(1, "Learner Diagnosis Input", "Ingestion")
    print(f"  {Style.CYAN}• Topic           :{Style.RESET} {target_problem.topic}")
    print(f"  {Style.CYAN}• Detected Flaw   :{Style.RESET} {Style.CORAL}{target_problem.error_type}{Style.RESET}")
    print(f"  {Style.CYAN}• Skill Level     :{Style.RESET} {target_problem.proficiency_level}")
    print(f"  {Style.CYAN}• Error Frequency :{Style.RESET} {target_problem.error_frequency} repeated occurrences")

    # Step 2: Retrieval
    draw_section(2, "Experiential Retrieval", "Retrieval Phase")
    best_case, sim_score, breakdown = retrieve_best_case(target_problem)
    
    print(f"  {Style.CYAN}• Best Match Case :{Style.RESET} {Style.BOLD}{best_case.case_id}{Style.RESET}")
    print(f"  {Style.CYAN}• Match Affinity  :{Style.RESET} {render_meter(sim_score)}")
    print(f"  {Style.SLATE}  └─ Breakdown   : {breakdown}{Style.RESET}")
    print(f"  {Style.CYAN}• Past Baseline   :{Style.RESET} \"{best_case.solution.intervention}\"")

    # Step 3: Reuse & Revise
    draw_section(3, "Solution Adaptation & Revision", "Pedagogical Tuning")
    adapted = adapt_solution(best_case, target_problem)
    
    print(f"  {Style.MINT}✔ Action Assigned :{Style.RESET} {adapted.intervention}")
    print(f"  {Style.MINT}✔ Practice Set    :{Style.RESET} {adapted.recommended_practice}")
    print(f"  {Style.MINT}✔ Dynamic Pacing  :{Style.RESET} {Style.GOLD}{adapted.difficulty_adjustment}{Style.RESET}")

    # Step 4: Retain
    draw_section(4, "Experiential Retention", "Continuous Learning")
    new_case_id = retain_case(target_problem, adapted)
    
    print(f"  {Style.LILAC}✦ Learning State  :{Style.RESET} Preserving experience into local case memory...")
    print(f"  {Style.LILAC}✦ Stored Key      :{Style.RESET} {Style.BOLD}{new_case_id}{Style.RESET}")
    print(f"  {Style.LILAC}✦ Memory Pool     :{Style.RESET} Case Base incremented to {Style.BOLD}{len(case_base)}{Style.RESET} active entries")
    print(f"\n{Style.SLATE}{'─' * 72}{Style.RESET}")

# CASE BASE VIEWER
def display_case_base() -> None:
    width = 72
    print(f"\n{Style.CYAN}╭{'─' * (width - 2)}╮{Style.RESET}")
    print(f"{Style.CYAN}│{Style.BOLD}{Style.WHITE} {'CURRENT ITS CASE BASE REPOSITORY'.center(width - 4)} {Style.RESET}{Style.CYAN}│{Style.RESET}")
    print(f"{Style.CYAN}╰{'─' * (width - 2)}╯{Style.RESET}")
    
    for case in case_base:
        p = case.problem
        s = case.solution
        print(f"\n  {Style.GOLD}[{case.case_id}]{Style.RESET} {Style.BOLD}{p.topic}{Style.RESET} | {Style.CORAL}{p.error_type}{Style.RESET} ({p.proficiency_level}, Freq: {p.error_frequency})")
        print(f"    {Style.SLATE}Action  :{Style.RESET} {s.intervention}")
        print(f"    {Style.SLATE}Practice:{Style.RESET} {s.recommended_practice}")
        print(f"    {Style.SLATE}Pacing  :{Style.RESET} {s.difficulty_adjustment}")
    
    print(f"\n{Style.SLATE}{'─' * 72}{Style.RESET}")

# INTERACTIVE CLI MAIN MENU
def main_menu():
    while True:
        draw_header(
            title="INTELLIGENT TUTORING SYSTEM (ITS)",
            subtitle="Case-Based Pedagogical Reasoning Engine",
            programmers=["Dianna Francesca M. Pardilla", "Justin D. Vergara"],
            section="CS0065 - AN41"
        )
        
        print(f"  {Style.BOLD}[1]{Style.RESET} Run Default Assessment Scenario")
        print(f"  {Style.BOLD}[2]{Style.RESET} Enter Custom Student Error (Solve & Retain)")
        print(f"  {Style.BOLD}[3]{Style.RESET} View Entire Case Base Repository ({len(case_base)} cases)")
        print(f"  {Style.BOLD}[4]{Style.RESET} Exit System")
        print(f"{Style.SLATE}{'─' * 72}{Style.RESET}")
        
        choice = input(f"{Style.GOLD}Select option [1-4]: {Style.RESET}").strip()

        if choice == "1":
            default_case = ProblemState(
                topic="Algebra",
                error_type="Formula Misuse",
                proficiency_level="Beginner",
                error_frequency=5
            )
            run_its_cbr_pipeline(default_case)
            input(f"\n{Style.DIM}Press Enter to return to main menu...{Style.RESET}")

        elif choice == "2":
            print(f"\n{Style.CYAN}--- Enter New Student Data ---{Style.RESET}")
            topic = input("Enter Topic (e.g., Algebra, Geometry, Calculus): ").strip().capitalize() or "Algebra"
            error = input("Enter Error Type (e.g., Formula Misuse, Sign Error, Unit Mismatch): ").strip().title() or "Sign Error"
            
            print("Proficiency Levels: [1] Beginner  [2] Intermediate  [3] Advanced")
            lvl_choice = input("Select level (1-3): ").strip()
            level_map = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
            level = level_map.get(lvl_choice, "Beginner")
            
            try:
                freq = int(input("Enter Error Frequency (1-10): ").strip())
            except ValueError:
                freq = 3
            
            custom_problem = ProblemState(topic, error, level, freq)
            run_its_cbr_pipeline(custom_problem)
            input(f"\n{Style.DIM}Press Enter to return to main menu...{Style.RESET}")

        elif choice == "3":
            display_case_base()
            input(f"\n{Style.DIM}Press Enter to return to main menu...{Style.RESET}")

        elif choice == "4":
            print(f"\n{Style.MINT}Exiting Intelligent Tutoring System. Goodbye!{Style.RESET}\n")
            break

        else:
            print(f"{Style.CORAL}Invalid choice! Please select 1, 2, 3, or 4.{Style.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()