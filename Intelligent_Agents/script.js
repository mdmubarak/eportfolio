const phrases = [
  'The government raised interest rates.',
  'The internet gives everyone a voice.',
  'The man saw the dog with the telescope.'
];

function createParseTree(sentence) {
  const tree = document.createElement('ul');
  const words = sentence.split(' ');

  let currentList = tree;
  let wordIndex = 0;

  while (wordIndex < words.length) {
    const word = words[wordIndex];
    const listItem = document.createElement('li');

    if (word.endsWith('.') || word.endsWith(',')) {
      word = word.slice(0, -1);
    }

    listItem.textContent = word;

    if (wordIndex > 0) {
      currentList.appendChild(listItem);
    }

    if (wordIndex < words.length - 1) {
      const newList = document.createElement('ul');
      listItem.appendChild(newList);
      currentList = newList;
    }

    wordIndex++;
  }

  return tree;
}

document.addEventListener('DOMContentLoaded', () => {
  const parseTreeContainer = document.getElementById('parse-tree');

  phrases.forEach(phrase => {
    const parseTree = createParseTree(phrase);
    parseTreeContainer.appendChild(parseTree);
  });
});
