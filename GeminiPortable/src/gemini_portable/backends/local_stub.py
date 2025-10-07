def get_response(prompt: str) -> str:
    """
    A deterministic LLM stub for sovereign generative AI.
    Produces predictable output based on specific keywords.
    This backend is the default and operates entirely offline.
    """
    prompt_lower = prompt.lower()
    if "axiomhive principles" in prompt_lower:
        return (
            "The AxiomHive principles are Determinism (H=0), Sovereignty (Local-First), "
            "Verifiable Integrity, Ethics-by-Default, and Offline-First."
        )
    elif "4d memory" in prompt_lower:
        return ("The 4D memory system conceptually organizes information across spatio-temporal and "
                "causal/counterfactual axes for advanced recall.")
    else:
        return f"Deterministic response to: '{prompt}' (Local LLM Stub)"
