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
Object.defineProperty(exports, "__esModule", { value: true });
var app_1 = require("firebase/app");
var auth_1 = require("firebase/auth");
var database_1 = require("firebase/database");
var config_js_1 = require("../../config.js");
var DatabaseService = (function () {
    function DatabaseService() {
        try {
            this.app = (0, app_1.initializeApp)(__assign({}, config_js_1.conf.firebase));
            var auth = (0, auth_1.getAuth)();
            (0, auth_1.signInWithEmailAndPassword)(auth, config_js_1.conf.authFirebase.email, config_js_1.conf.authFirebase.password).catch(function (error) {
                var code = error.code, message = error.message;
                console.log("".concat(code, " - ").concat(message));
            });
            this.db = (0, database_1.getDatabase)(this.app);
            console.log('Инициализированно');
        }
        catch (err) {
            console.log(err);
            console.error('Application works without database!!');
        }
    }
    DatabaseService.prototype.getSavedAds = function (taskId) {
        var _this = this;
        return new Promise(function (resolve, reject) {
            (0, database_1.get)((0, database_1.child)((0, database_1.ref)(_this.db), 'ads/' + taskId)).then(function (snapshot) {
                if (snapshot.exists()) {
                    resolve(snapshot.val() || {});
                }
                else {
                    reject("No data available");
                }
            }).catch(function (error) {
                reject(error);
            });
        });
    };
    DatabaseService.prototype.setNewAd = function (path, ad) {
        var _this = this;
        return new Promise(function (resolve, reject) {
            (0, database_1.set)((0, database_1.ref)(_this.db, path + '/' + ad.id), ad).then(function () { return resolve(''); })
                .catch(function (error) {
                reject(error);
            });
        });
    };
    DatabaseService.prototype.getTasks = function () {
        var _this = this;
        return new Promise(function (resolve, reject) {
            (0, database_1.get)((0, database_1.child)((0, database_1.ref)(_this.db), 'tasks')).then(function (snapshot) { return resolve(snapshot.val()); })
                .catch(function (err) {
                reject(err);
            });
        });
    };
    DatabaseService.prototype.subscribeToTaskChange = function () {
        var _this = this;
        var activatePause = true;
        return new Promise(function (resolve) {
            (0, database_1.onChildChanged)((0, database_1.ref)(_this.db, 'tasks'), function (sn) { return resolve(sn.val()); });
            (0, database_1.onChildMoved)((0, database_1.ref)(_this.db, 'tasks'), function (sn) { return resolve(sn.val()); });
            (0, database_1.onChildRemoved)((0, database_1.ref)(_this.db, 'tasks'), function (sn) { return resolve(sn.val()); });
            (0, database_1.onChildAdded)((0, database_1.ref)(_this.db, 'tasks'), function (sn) {
                setTimeout(function () {
                    activatePause = false;
                });
                if (!activatePause) {
                    resolve(sn.val());
                }
            });
        });
    };
    return DatabaseService;
}());
var db = new DatabaseService();
exports.default = db;
//# sourceMappingURL=database.js.map