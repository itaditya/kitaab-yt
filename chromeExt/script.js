console.log('Kitab Starting');
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
    let { responseURL } = xhr;
    if(responseURL && responseURL.startsWith('https://www.youtube.com/api/timedtext')){
      console.log(responseURL);
      init(responseURL);
    }
  }
});

function init(responseURL) {
  const videoId = window.location.search.substr(3);
  console.log(responseURL);
  const body = {
    id: videoId,
    url: responseURL
  };
  sendVideoData(JSON.stringify(body), (data) => {
    console.log(data);
  })
}

document.querySelector('.ytp-subtitles-button').click();
document.querySelector('.ytp-subtitles-button').click();

function sendVideoData(body, cb) {
  fetch("https://49afc650.ngrok.io/parsing/parse.php", {
      method: "POST",
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
