//innerHTML, textContent
document.addEventListener('DOMContentLoaded', function(){
    //<a id="inner">要素のclickイベントリスナー
    document.getElementById('inner').addEventListener('click', function(e){
        window.alert('#innerリスナーが発生しました。');
    }, false);

    //<a id="inner">要素のclickイベントリスナー
    document.getElementById('inner').addEventListener('click', function(e){
        window.alert('#innerリスナー2が発生しました。');
    }, false);

    //thisの参照先
    var data = {
        title: 'Javaポケットリファレンス',
        price: 2680,
        handleEvent : function(){
            console.log(this.title + '/' + this.price + '円');
        }
    }
    document.getElementById('btn').addEventListener('click', data, false);

    var timer = window.setInterval(
        //現在の時刻を<div id="result">要素に表示(5000ミリ秒ごとに更新)
        function(){
            var dat = new Date();
            document.getElementById('result').textContent = dat.toLocaleTimeString();
        }
    , 500);
    //ボタンクリック時にタイマー処理を停止
    document.getElementById('btn').addEventListener('click', function(){
        window.clearInterval(timer);
    }, false);

    //オブジェクトを表示
    var obj_btn = document.getElementById('btn');
    console.log(obj_btn);
    console.log(obj_btn.value);
    console.dir(obj_btn);

    //ストレージの操作
    var storage = localStorage;
    storage.setItem('fruit1','リンゴ');
    storage.fruit2 = 'みかん';
    storage['fruit3'] = 'ぶどう';
    console.log(storage.getItem('fruit1'));
    console.log(storage.fruit2);
    console.log(storage['fruit3']);
}, false);
