def build_tech_prompt(tech_stack, experience):
    return f"""
    You are an AI hiring assistant for a recruitment agency.
    Generate 3 technical interview questions that assess intermediate-level proficiency 
    in the following technologies: {tech_stack}.
    The candidate has {experience} years of experience.
    
    Questions should be concise, focused, and cover both theoretical and practical aspects.
    """
