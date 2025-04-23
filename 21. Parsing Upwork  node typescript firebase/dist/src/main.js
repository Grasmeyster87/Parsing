"use strict";
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
var cron_1 = require("cron");
var avito_js_1 = require("./helpers/avito.js");
var database_js_1 = require("./helpers/database.js");
var utils_js_1 = require("./helpers/utils.js");
function createJob(task) {
    var _this = this;
    console.log('Создаю задачу ' + task.id);
    return new cron_1.CronJob(task.cron, function () { return __awaiter(_this, void 0, void 0, function () {
        var avito, newIds, _i, newIds_1, id, err_1;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    avito = new avito_js_1.Avito(task);
                    console.log('Запускаю задачу ' + task.id);
                    _a.label = 1;
                case 1:
                    _a.trys.push([1, 8, , 9]);
                    return [4, avito.getAdsIds()];
                case 2:
                    newIds = _a.sent();
                    _i = 0, newIds_1 = newIds;
                    _a.label = 3;
                case 3:
                    if (!(_i < newIds_1.length)) return [3, 7];
                    id = newIds_1[_i];
                    return [4, database_js_1.default.setNewAd(task.id, avito.updateAds[id])];
                case 4:
                    _a.sent();
                    return [4, (0, utils_js_1.pause)(300)];
                case 5:
                    _a.sent();
                    _a.label = 6;
                case 6:
                    _i++;
                    return [3, 3];
                case 7: return [3, 9];
                case 8:
                    err_1 = _a.sent();
                    console.error(err_1);
                    return [3, 9];
                case 9: return [2];
            }
        });
    }); });
}
function run() {
    return __awaiter(this, void 0, void 0, function () {
        var jobs, fullTasks, _a, _b, err_2, _i, fullTasks_1, task, job;
        return __generator(this, function (_c) {
            switch (_c.label) {
                case 0:
                    jobs = [];
                    return [4, (0, utils_js_1.pause)(5000)];
                case 1:
                    _c.sent();
                    fullTasks = [];
                    _c.label = 2;
                case 2:
                    _c.trys.push([2, 4, , 5]);
                    _b = (_a = Object).values;
                    return [4, database_js_1.default.getTasks()];
                case 3:
                    fullTasks = _b.apply(_a, [_c.sent()]);
                    console.log('Получен список задач');
                    return [3, 5];
                case 4:
                    err_2 = _c.sent();
                    console.error(err_2);
                    return [3, 5];
                case 5:
                    for (_i = 0, fullTasks_1 = fullTasks; _i < fullTasks_1.length; _i++) {
                        task = fullTasks_1[_i];
                        job = createJob(task);
                        job.start();
                        jobs.push(job);
                    }
                    database_js_1.default.subscribeToTaskChange().then(function () {
                        jobs.forEach(function (j) { return j.stop(); });
                        run();
                    });
                    return [2];
            }
        });
    });
}
run();
//# sourceMappingURL=main.js.map