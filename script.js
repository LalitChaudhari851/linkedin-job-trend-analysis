
async function loadJSON(url) {
  const res = await fetch(url);
  return res.json();
}

function renderSkillsTable(data) {
  const table = document.getElementById('skillsTable');
  let html = "<tr><th>City</th><th>Skill</th><th>Count</th></tr>";
  data.forEach(row => {
    html += `<tr><td>${row.city}</td><td>${row.skills}</td><td>${row.count}</td></tr>`;
  });
  table.innerHTML = html;
}

function renderMatrixTable(data) {
  const table = document.getElementById('matrixTable');
  const roles = Object.values(data)[0] ? Object.keys(Object.values(data)[0]) : [];
  let html = "<tr><th>Skill</th>" + roles.map(r => `<th>${r}</th>`).join('') + "</tr>";
  for (let skill in data) {
    html += `<tr><td>${skill}</td>` + roles.map(r => `<td>${data[skill][r]}</td>`).join('') + "</tr>";
  }
  table.innerHTML = html;
}

async function init() {
  const skillsData = await loadJSON("data/top_skills_by_city.json");
  renderSkillsTable(skillsData);
  const matrixData = await loadJSON("data/skill_vs_role.json");
  renderMatrixTable(matrixData);
}

init();
