console.log('test');
function addXMLRequestCallback(callback) {
  let oldSend, i;
  if (XMLHttpRequest.callbacks) {
    XMLHttpRequest.callbacks.push(callback);
  } else {
    XMLHttpRequest.callbacks = [callback];
    oldSend = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.send = function () {
      for (i = 0; i < XMLHttpRequest.callbacks.length; i++) {
        XMLHttpRequest.callbacks[i](this);
      }
      oldSend.apply(this, arguments);
    }
  }
}

addXMLRequestCallback(xhr => {
  xhr.onload = function (e) {
    if(xhr.responseURL.startsWith('https://www.youtube.com/api/timedtext')){
      init(xhr.responseURL);
    }
  }
});

function init(responseURL) {
  const videoId = window.location.search.substr(3);
  console.log(responseURL);
  sendVideoData({
    id: videoId,
    url: responseURL
  }, (data) => {
    console.log(data);
  })
}
init();

function sendVideoData(body, cb) {
  fetch("https://49afc650.ngrok.io/parsing/parse.php", {
      method: "POST",
      headers: {
        "Content-type": "application/json"
      },
      body
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
