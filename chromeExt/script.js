console.log('Kitaab Opening');
const videoId = window.location.search.substr(3);

let flag = false;

function genHtml(imgUrl = 'https://wordart.com/static/img/word_cloud.png') {
  return `
  <h1>Kitaab</h1>
  <input id="searchForm" type="text" value="pwa"/>
  <button id="searchBtn" onclick="searchWord()">Search</button>
  </br>
`
}
  // <img style="width: 100%;" src="${imgUrl}" alt="" />

function searchWord() {
  const word = document.querySelector('#searchForm').value;
  console.log(word);
  sendSearchWord({
    id: videoId,
    word
  }, (data) => {
    const ytplayer = document.getElementById("movie_player");
    console.log(data);
    ytplayer.seekTo(data.time || 3);
  })
}

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
    let {
      responseURL
    } = xhr;
    if (responseURL && responseURL.startsWith('https://www.youtube.com/api/timedtext')) {
      console.log(responseURL);
      init(responseURL);
    }
  }
});

function init(responseURL) {
  console.log(responseURL);
  const body = {
    id: videoId,
    url: responseURL
  };
  sendVideoData(JSON.stringify(body), (data) => {
    console.log(data);
    document.querySelector('#related').insertAdjacentHTML('afterBegin', genHtml());
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

function sendSearchWord(body, cb) {
  fetch("https://49afc650.ngrok.io/parsing/search.php", {
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
