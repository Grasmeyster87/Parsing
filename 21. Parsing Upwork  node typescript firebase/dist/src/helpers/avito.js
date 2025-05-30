"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Avito = void 0;
var axios_1 = require("axios");
var jsdom_1 = require("jsdom");
var JSDOM = jsdom_1.default.JSDOM;
var database_js_1 = require("./database.js");
var utils_js_1 = require("./utils.js");
var Avito = (function () {
    function Avito(task) {
        this.baseUrl = 'https://www.avito.ru';
        this._task = task;
    }
    Object.defineProperty(Avito.prototype, "updateAds", {
        get: function () {
            return this._updateAds;
        },
        enumerable: false,
        configurable: true
    });
    Avito.prototype.getAdsIds = function () {
        return __awaiter(this, void 0, void 0, function () {
            var savedAds, _i, _a, city, html, newIds;
            return __generator(this, function (_b) {
                switch (_b.label) {
                    case 0: return [4, database_js_1.default.getSavedAds(this._task.id)];
                    case 1:
                        savedAds = _b.sent();
                        _i = 0, _a = this._task.cities;
                        _b.label = 2;
                    case 2:
                        if (!(_i < _a.length)) return [3, 5];
                        city = _a[_i];
                        return [4, this.fetchAds(this.baseUrl, city, this._task.category)];
                    case 3:
                        html = _b.sent();
                        this._updateAds = __assign(__assign({}, this._updateAds), this.getAdsFromDom(html));
                        console.log('Добавитл информацию для говрода ' + city);
                        _b.label = 4;
                    case 4:
                        _i++;
                        return [3, 2];
                    case 5:
                        newIds = (0, utils_js_1.compareCollections)(savedAds, this._updateAds);
                        console.log('Обнаружено ' + newIds.length + ' новых объявлений');
                        return [2, newIds];
                }
            });
        });
    };
    Avito.prototype.fetchAds = function (baseUrl, city, category) {
        return __awaiter(this, void 0, void 0, function () {
            var html, resp, error_1;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0:
                        _a.trys.push([0, 2, , 3]);
                        return [4, axios_1.default.get("".concat(baseUrl, "/").concat(city, "/").concat(category, "?q=airtag&s=104"), { responseType: 'document' })];
                    case 1:
                        resp = _a.sent();
                        html = resp.data;
                        return [3, 3];
                    case 2:
                        error_1 = _a.sent();
                        if (axios_1.default.isAxiosError(error_1)) {
                            console.log(error_1);
                        }
                        else {
                            console.log(error_1);
                        }
                        return [3, 3];
                    case 3: return [2, html];
                }
            });
        });
    };
    Avito.prototype.getAdsFromDom = function (html) {
        var dom = new JSDOM(html);
        var document = dom.window.document;
        var items = document.querySelectorAll('[data-marker=item]');
        var ads = {};
        items.forEach(function (node) {
            ads[node.id] = {
                id: node.id,
                title: node.querySelector('[itemprop=name]').textContent,
                price: Number(node.querySelector('[itemprop=price]').getAttribute('content')),
                url: node.querySelector('[itemprop=url]').getAttribute('href'),
            };
        });
        return ads;
    };
    return Avito;
}());
exports.Avito = Avito;
//# sourceMappingURL=avito.js.map