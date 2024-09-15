# Define a dictionary to map side hustles to their respective keywords
side_hustles = {
    "Scriptwriter": ["Creative writing", "Screenwriting", "Story development", "Dialogue creation", "Narrative structure", "English", "Content", "Media"],
    "Prompt Engineer": ["Natural language processing", "AI", "Model optimization", "GPT-3/4", "Data analysis", "Computer Science", "Programming", "Technical"],
    "Medium Content Writer": ["Blog writing", "SEO optimization", "Content strategy", "Article development", "Copywriting", "English", "Content", "Media"],
    "Graphic Designer": ["Adobe Creative Suite", "Branding", "Visual communication", "Typography", "Layout design", "Art", "Creativity", "Technical"],
    "Animator": ["2D/3D animation", "Motion graphics", "Storyboarding", "After Effects", "Character design", "Programming", "Computer science", "Technical"],
    "Photographer": ["Photo editing", "Lightroom", "Event photography", "Composition", "Lighting techniques", "Entrepreneurship", "Content", "Media"],
    "3D Printing": ["CAD", "Additive manufacturing", "3D modeling", "Prototyping", "AutoCAD", "Graphic Design", "Technical", "Math"],
    "Virtual Bookkeeper": ["QuickBooks", "Accounts payable/receivable", "Financial reporting", "Reconciliation", "Data entry", "Analysis", "Management", "Technical"],
    "Podcast Host": ["Public speaking", "Audio editing", "Content creation", "Interviewing skills", "Audience engagement", "Communication", "Content", "Media"],
    "Online Tutor": ["Curriculum development", "Lesson planning", "Subject expertise", "Virtual teaching platforms", "Student engagement", "STEM", "Honor Roll", "High School"],
    "Voiceover Artist": ["Voice modulation", "Audio recording", "Diction", "Script interpretation", "Studio equipment", "Content", "Media", "Editing"],
    "Web Developer": ["HTML/CSS/JavaScript", "Full-stack development", "Responsive design", "API integration", "Front-end/back-end development", "Bootstrap", "VSCode", "Django"],
    "Babysitter": ["Childcare", "CPR certification", "Time management", "Conflict resolution", "Activity planning", "Customer Service", "Organization", "Adaptability"],
    "Content Editor": ["Proofreading", "Copy editing", "Grammar and syntax", "Style guides", "Attention to detail", "Content", "Media", "Writing"],
    "Video Editor": ["Final Cut Pro", "Storytelling", "Color grading", "Video transitions", "Timeline management", "Software", "Technical", "Media"],
    "Dog Walker": ["Pet care", "Time management", "Route planning", "Animal behavior", "Reliability", "Organization", "Customer Service", "Adaptability"]
}

# Dictionary to hold the side hustle names as keys and their respective scores
side_hustle_scores = {side_hustle: 0 for side_hustle in side_hustles}

# Open the file in read mode
with open('uploaded_resume.pdf', 'r') as file:
    content = file.read()
    words = content.split()

    # Loop through words in file
    for word in words:
        # Check if word matches any keywords for each side hustle
        for side_hustle, keywords in side_hustles.items():
            if word in keywords:
                side_hustle_scores[side_hustle] += 1

# Print the side hustles with their scores
for hustle, score in side_hustle_scores.items():
    print(f"Side hustle: {hustle}, Score: {score}")
