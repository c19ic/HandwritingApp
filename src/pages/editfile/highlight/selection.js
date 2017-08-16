// Get selected text / 選択部分のテキストを取得
$('#sel-text').click(function(){
  $('#result').text($.selection());
});

// Get selected html / 選択部分のHTMLを取得
$('#sel-html').click(function(){
  $('#result').text($.selection('html'));
});