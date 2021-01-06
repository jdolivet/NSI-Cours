/*jslint node:true*/

module.exports = function (grunt) {

    'use strict';

    grunt.loadNpmTasks('grunt-jslint'); // load the task

    grunt.initConfig({

        jslint: {
            files: [
                'Gruntfile.js',
                'js/grain.js',
                'js/main.js',
                'meta.json'
            ],
            options: {
                failOnError: true
            }
        }

    });

    // default task.
    grunt.registerTask('default', ['jslint', 'meta_json_pretty_print']);

    // Travis CI task.
    grunt.registerTask('test', 'jslint');

    grunt.registerTask('meta_json_pretty_print', function () {
        var metadata = grunt.file.readJSON('meta.json');
        grunt.file.write('meta.json', JSON.stringify(metadata, null, 4));
    });

};
