["name", "company", "salary_from", "salary_to", "currency", "experience", "url"],
(.items[] | [
    .name,
    .employer.name,
    (.salary.from // "null"),
    (.salary.to // "null"),
    (.salary.currency // "null"),
    .experience.name,
    .alternate_url
]) | @csv
