let toggle = false;
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === 'clicked_browser_action') {
    toggle = !toggle;
    if (toggle) {
    } else {
      init();
    }
  }
});

function init() {
  console.log(window.location.href);
  const videoId = window.location.search.substr(3);
  sendVideoData({}, (data) => {
    console.log(data);
  })
}
// init();

function sendVideoData(body, cb) {
  fetch("http://127.0.0.1:8080/manifest.json", {
      method: "GET",
      headers: {
        "Content-type": "application/json"
      }
    })
    .then(res => {
      if (res.status !== 200) {
        console.error("Couldn't connect to server");
        return;
      }
      res
        .json()
        .then(data => {
          cb(data);
        })
        .catch(err => {
          console.log(err);
        });
    })
    .catch(err => {
      console.log(err);
    })
}
// http://127.0.0.1:8080/manifest.json
