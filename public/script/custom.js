"use strict";

function getWord() {
  var rnd = Math.random();
  var word, word_type, label;

  if (rnd < 0.4) {
    word = words_list[Math.floor(Math.random() * words_list.length)];
    word_type = "new word";
    label = "";
  } else if (rnd < 0.65) {
    word = learning[Math.floor(Math.random() * learning.length)];
    word_type = "learning";
    label = "label-danger";
  } else if (rnd < 0.9) {
    word = reviewing[Math.floor(Math.random() * reviewing.length)];
    word_type = "reviewing";
    label = "label-warning";
  } else {
    word = mastered[Math.floor(Math.random() * mastered.length)];
    word_type = "mastered";
    label = "label-success";
  }

  if (!word) return getWord();
  return {
    word: word,
    word_type: word_type,
    label: label
  };
}

function reset($elem) {
  $elem.before($elem.clone(true));
  var $newElem = $elem.prev();
  $elem.remove();
  return $newElem;
}

function showWord() {
  var w = getWord();
  var word = w.word,
    word_type = w.word_type,
    label = w.label;
  $(".flashcard-word").text(word);
  $(".flashcard-status").text(word_type);
  $(".label-flashcard")
    .text(word_type)
    .attr("class", "label label-flashcard " + label);
  var flashcard_text = "<ul>";
  words[word].forEach(function(text) {
    flashcard_text += "<li>".concat(text, "</li>");
  });
  flashcard_text += "</ul>";
  $(".flashcard-text").html(flashcard_text);
}

$(document).ready(function() {
  // var l = localStorage.getItem("learning"),
  //   r = localStorage.getItem("reviewing"),
  //   m = localStorage.getItem("mastered"),
  //   w = localStorage.getItem("words");
  // if (l) learning = JSON.parse(l);
  // if (r) reviewing = JSON.parse(r);
  // if (m) mastered = JSON.parse(m);
  // if (w) {
  //   words = JSON.parse(w);
  //   words_list = Object.keys(words);
  // } else {
  //   localStorage.setItem("words", JSON.stringify(words));
  // }
  reflectInBars();
  showWord();
});
var learning = [],
  reviewing = [],
  mastered = [],
  words_list = Object.keys(words);
$(document).on("click", ".know-word", function(e) {
  e.preventDefault();
  var status = $(".back .flashcard-status").text();
  var word = $(".back .flashcard-word").text();

  switch (status) {
    case "new word":
      words_list = $.grep(words_list, function(value) {
        return value !== word;
      });
      mastered.push(word);
      break;

    case "reviewing":
      reviewing = $.grep(reviewing, function(value) {
        return value !== word;
      });
      mastered.push(word);
      break;

    case "learning":
      learning = $.grep(learning, function(value) {
        return value !== word;
      });
      reviewing.push(word);
      break;
  }

  showWord();
  reflectInBars();
});
$(document).on("click", ".dont-know-word", function(e) {
  e.preventDefault();
  var status = $(".back .flashcard-status").text();
  var word = $(".back .flashcard-word").text();

  switch (status) {
    case "mastered":
      learning.push(word);
      mastered = $.grep(mastered, function(value) {
        return value !== word;
      });
      break;

    case "new word":
      learning.push(word);
      words_list = $.grep(words_list, function(value) {
        return value !== word;
      });
      break;

    case "reviewing":
      learning.push(word);
      reviewing = $.grep(reviewing, function(value) {
        return value !== word;
      });
      break;
  }

  showWord();
  reflectInBars();
});

function reflectInBars() {
  var totalWords = Object.keys(words).length;
  var totalMasteredWords = mastered.length;
  var totalReviewingWords = reviewing.length;
  var totalLearningWords = learning.length;
  $("#mastered-flashcards-progress").css(
    "width",
    (totalMasteredWords / totalWords) * 100 + "%"
  );
  $("#mastered-flashcards-count").text(totalMasteredWords);
  $("#reviewing-flashcards-progress").css(
    "width",
    (totalReviewingWords / totalWords) * 100 + "%"
  );
  $("#reviewing-flashcards-count").text(totalReviewingWords);
  $("#learning-flashcards-progress").css(
    "width",
    (totalLearningWords / totalWords) * 100 + "%"
  );
  $("#learning-flashcards-count").text(totalLearningWords);
}
