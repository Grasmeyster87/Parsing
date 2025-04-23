"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.pause = pause;
exports.compareCollections = compareCollections;
function pause(val) {
    if (val === void 0) { val = 500; }
    return new Promise(function (resolve) {
        setTimeout(resolve, val);
    });
}
function compareCollections(src, updates) {
    return Object.keys(updates).filter(function (key) { return !src[key]; });
}
//# sourceMappingURL=utils.js.map