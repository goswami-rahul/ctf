'use strict';
/** @type {!Array} */
var a = ["2-4", "substring", "4-7", "getItem", "deleteItem", "12-14", "0-2", "setItem", "9-12", "^7M", "updateItem", "bb=", "7-9", "14-16", "localStorage"];
(function(data, i) {
  /**
   * @param {number} isLE
   * @return {undefined}
   */
  var write = function(isLE) {
    for (; --isLE;) {
      data["push"](data["shift"]());
    }
  };
  write(++i);
})(a, 120);
/**
 * @param {string} level
 * @param {?} ai_test
 * @return {?}
 */

/**
 * @param {!Object} results
 * @return {?}
 */
function CheckPassword(results) {
  /** @type {!Array} */
  var easing = ["localStorage", "getItem", "setItem", "deleteItem", "updateItem"];
  window["localStorage"]["setItem"]("9-12", "BE*");
  window["localStorage"]["setItem"]("4-7", "bb=");
  window["localStorage"]["setItem"]("0-2", "5W");
  window["localStorage"]["setItem"]("16", "^7M");
  window["localStorage"]["setItem"]("12-14", "pg");
  window["localStorage"]["setItem"]("7-9", "+n");
  window["localStorage"]["setItem"]("14-16", "4t");
  window["localStorage"]["setItem"]("2-4", "$F");
  if (window["localStorage"]["getItem"]("9-12") === results["substring"](9, 12)) {
    if (window["localStorage"]["getItem"]("4-7") === results["substring"](4, 7)) {
      if (window["localStorage"]["getItem"]("0-2") === results["substring"](0, 2)) {
        if (window["localStorage"]["getItem"]("16") === results["substring"](16)) {
          if (window["localStorage"]["getItem"]("12-14") === results["substring"](12, 14)) {
            if (window["localStorage"]["getItem"]("7-9") === results["substring"](7, 9)) {
              if (window["localStorage"]["getItem"]("14-16") === results["substring"](14, 16)) {
                if (window["localStorage"]["getItem"]("2-4") === results["substring"](2, 4)) {
                  return !![];
                }
              }
            }
          }
        }
      }
    }
  }
  return ![];
}
;