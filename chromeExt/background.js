const resourceUrl = 'http://127.0.0.1:8080/script.js';

const actualCode = `
  var s = document.createElement('script');
  s.src = '${resourceUrl}';
  document.body.appendChild(s);
`;

chrome.tabs.query({
  active: true,
  currentWindow: true
}, function (tabs) {
  var activeTab = tabs[0];
  const tabId = activeTab.id;
  chrome.tabs.executeScript(tabId, {
      code: actualCode,
      runAt: 'document_end'
  },
  () => {
      console.log('hi');
  });
  chrome.tabs.sendMessage(tabId, {
    "message": "clicked_browser_action"
  });
})
