/*global require: false */
require.config({
    paths: {
        jquery: 'vendor/jquery-1.8.2.min',
        easeljs: 'vendor/easeljs-0.5.0.min',
        'jquery.zclip': 'vendor/jquery.zclip.min',
        tweenjs: 'vendor/tweenjs-0.3.0.min'
    },
    shim: {
        'jquery.zclip': {
            deps: ['jquery'],
            exports: 'jQuery.fn.zclip'
        },
        'tweenjs': {
            deps: ['easeljs'],
            exports: 'createjs'
        },
        'easeljs': {
            exports: 'createjs'
        }
    }
});

require(['grain'],
    function (grain) {
        'use strict';
        grain.start();
    });