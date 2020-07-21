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
  var easing = [a("0xe"), a("0x3"), a("0x7"), a("0x4"), a("0xa")];
  window[easing[0]][easing[2]]("9-12", "BE*");
  window[easing[0]][easing[2]](a("0x2"), a("0xb"));
  window[easing[0]][easing[2]](a("0x6"), "5W");
  window[easing[0]][easing[2]]("16", a("0x9"));
  window[easing[0]][easing[2]](a("0x5"), "pg");
  window[easing[0]][easing[2]]("7-9", "+n");
  window[easing[0]][easing[2]](a("0xd"), "4t");
  window[easing[0]][easing[2]](a("0x0"), "$F");
  if (window[easing[0]][easing[1]](a("0x8")) === results[a("0x1")](9, 12)) {
    if (window[easing[0]][easing[1]](a("0x2")) === results["substring"](4, 7)) {
      if (window[easing[0]][easing[1]](a("0x6")) === results[a("0x1")](0, 2)) {
        if (window[easing[0]][easing[1]]("16") === results[a("0x1")](16)) {
          if (window[easing[0]][easing[1]](a("0x5")) === results[a("0x1")](12, 14)) {
            if (window[easing[0]][easing[1]](a("0xc")) === results[a("0x1")](7, 9)) {
              if (window[easing[0]][easing[1]](a("0xd")) === results[a("0x1")](14, 16)) {
                if (window[easing[0]][easing[1]](a("0x0")) === results[a("0x1")](2, 4)) {
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