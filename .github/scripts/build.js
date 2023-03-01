const fs = require('fs');
const data = require('../../data.json');

const TPL_FILE = './.github/tpl.md';
const TARGET = './README.md';

const tpl = getTemplate(TPL_FILE);

const categories = {};

data.repositories.sort((a, b) => {
    const nameA = a.name.toUpperCase();
    const nameB = b.name.toUpperCase();
    if (nameA < nameB) {
        return -1;
    }
    if (nameA > nameB) {
        return 1;
    }
    return 0;
}).forEach(repo =>
    repo.technologies.forEach(tech => {
        if (!categories.hasOwnProperty(tech)) {
            categories[tech] = [];
        }
        categories[tech].push(repo);
    }))

const sortedCategories = Object.fromEntries(Object.entries(categories).sort((a, b) => {
    const nameA = a[0].toUpperCase();
    const nameB = b[0].toUpperCase();
    if (nameA < nameB) {
        return -1;
    }
    if (nameA > nameB) {
        return 1;
    }
    return 0;
}));

const toc = Object.keys(sortedCategories)
    .map(t => `- [${t}](#${data.technologies[t] || t.toLowerCase()})`)
    .join('\n');

const content = Object.keys(sortedCategories)
    .map(category => {
        const repos = sortedCategories[category].map(repo => `- [${repo.name}](${repo.link}) _(label: ${repo.label || 'n/a'})_ <br> ${repo.description}`).join('\n')
        return `## ${category}\n\n${repos}\n`
    }).join('\n');

const sponsorList = data.sponsors.map(sponsor => `<td align="center"><a href="${sponsor.link}"><img src="${sponsor.image}" width="60px;" alt=""/><br/><sub><b>${sponsor.name}</b></sub></a></td>`)
const sponsorRows = Math.ceil(sponsorList.length / 6);

let sponsors = '';

for (let i = 1; i <= sponsorRows; i++) {
    sponsors += '<tr>';
    for(let j = 0; j < 6; j++) {
        if (sponsorList.length > i*j) {
            sponsors += sponsorList[i*j];
        } else if (sponsorRows > 1) {
            sponsors += '<td></td>'
        }
    }
    sponsors += '</tr>';
}

sponsors = `<table>${sponsors}</table>`

saveFile(TARGET, render(tpl, { toc, content, sponsors }));

function getTemplate(file) {
    return fs.readFileSync(file).toString();
}

function saveFile(file, contents) {
    return fs.writeFileSync(file, contents);
}

function render(template, variables) {
    Object
        .entries(variables)
        .forEach(([key, value]) => {
            template = template.replace(new RegExp(`<% ${key} %>`, 'g'), value);
        });
    return template;
}
