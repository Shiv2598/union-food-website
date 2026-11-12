const fs = require('fs');
const jsCode = fs.readFileSync('js/script.js', 'utf8');

const window = {};
const document = {
  querySelectorAll: () => [],
  getElementById: () => null,
  addEventListener: () => {}
};
const localStorage = {
  getItem: () => null,
  setItem: () => {}
};

eval(jsCode);

console.log('Search Data entries count:', window.searchData.length);

const testQueries = [
  'Oil', 'Mustard Oil', 'Atta', 'Wheat', 'Dal', 'Spices',
  'Snacks', 'Juice', 'Beverages', 'Discount', 'Offers',
  'Recipes', 'Certification', 'About Us', 'Contact'
];

testQueries.forEach(q => {
  const qLower = q.toLowerCase();
  const tokens = qLower.split(/\s+/).filter(Boolean);
  const matches = window.searchData.filter(item => {
    const text = (item.name + ' ' + item.category + ' ' + item.description + ' ' + (item.keywords || []).join(' ')).toLowerCase();
    return tokens.some(t => text.includes(t));
  });
  console.log(`Query: "${q}" -> ${matches.length} matches (Top: ${matches[0] ? matches[0].name : 'None'})`);
});
