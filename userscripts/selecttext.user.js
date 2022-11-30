// ==UserScript==
// @name        Select Text
// @namespace   Violentmonkey Scripts
// @match       https://adventofcode.com/*/day/**
// @grant       none
// @version     1.0
// @author      -
// @icon         https://adventofcode.com/favicon.png
// @description 2021-12-02, 3:45:42 p.m.
// ==/UserScript==

/**
 * Select entire code box on double click
 */

 (function() {
    'use strict';
    
    function selectBlock(e) {
      window.getSelection().selectAllChildren(e.target);
    }
    
    let codes = document.getElementsByTagName("code")
    
    for (let i=0; i<codes.length; i++) {
      codes[i].addEventListener("dblclick", selectBlock);
    }
  })();
  