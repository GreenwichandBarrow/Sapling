"""Pipeline manager handler: trigger daily pipeline review on session start."""

from ..models import HandlerResult


def pipeline_pulse(input_data: dict) -> HandlerResult:
    """SessionStart: inject context telling Claude to run pipeline-manager skill."""
    return HandlerResult(
        additional_context=(
            "PIPELINE MANAGER: Run the /pipeline-manager skill now. "
            "Scan yesterday's calendar, email, and vault for activity signals, "
            "match them against Attio pipeline entries, and present recommended "
            "stage changes for Kay to approve or reject. Send a Slack nudge first."
        )
    )
