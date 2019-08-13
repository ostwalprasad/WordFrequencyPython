var words_list = Object.keys(words);
var index = 0;

$(document).ready(() => {
  showWord(words_list[index]);
});

$(".next-word").on("click", e => {
  if (words_list[index]) {
    $(".flashcard").removeClass("flipped");
    showWord(words_list[index]);
  } else {
    $(".alert-message").show();
    $(".next-word").hide();
  }
});

function showWord(word) {
  $(".flashcard-word").text(word);

  let flashcard_text = "<ul>";
  words[word].forEach(text => {
    flashcard_text += `<li>${text}</li>`;
  });
  flashcard_text += "</ul>";
  $(".flashcard-text").html(flashcard_text);
  index++;

  $(".word-counter").text(`${index} of ${words_list.length}`);
}
