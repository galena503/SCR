var sol_app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {

        disp: {
            timer: true,
            flash: true,
            tune: true,
            set: true
        },
        timer: {
            disp: 'true',
            text: 'おおまじか',
            folder: '',
            file: '',
            sec: ''
        },

        schedule: "",
        s_change: true,
        add_code: {
            d: "",
            f: "",
            i: ""
        }
    },
    methods: {
        main_display_change: function (display_name) {
            for (key in this.UI.main_display) {
                this.UI.main_display[key] = false;
            }
            this.UI.main_display[display_name] = true;
        },
        get_0_sch: function () {
            if (sol_app.schedule === "") {
                // データがない場合取得のみを行う
                this.get_0_fast();
            } else if (!sol_app.s_change) {
                this.get_0_change();
            }
        },
        get_0_fast: function () {
            axios
                .get(location.origin + '/api/0/', )
                .then(function (res) {
                    sol_app.schedule = res.data;
                })
                .catch(function (err) {
                    console.log(err);
                });
        },
        get_0_change: function () {
            send_str = this.schedule;
            axios
                .post(location.origin + '/api/0/change', send_str)
                .then(function (res) {
                    sol_app.schedule = res.data;
                })
                .catch(function (err) {
                    console.log(err);
                });
        },
        post_d_test: function () {
            sol_app.schedule.tasks.forEach(function (task, index) {
                var t_i = index;
                if (task.key === sol_app.add_code.d) {
                    task.items.forEach(function (item, index) {
                        var i_i = index;
                        if (item.f + '.py' === sol_app.add_code.f) {
                            sol_app.schedule.tasks[t_i].items[i_i].s = sol_app.add_code.i;
                        }
                    });
                }
            });

        },
        del_task: function (t_index,i_index) {
            console.log(t_index + "-" + i_index);
            if(sol_app.schedule.tasks[t_index].items.length == 1){
                sol_app.schedule.tasks.splice(t_index, 1);
            }else{
                sol_app.schedule.tasks[t_index].items.splice(i_index, 1);
            }
        }

    },
    beforeUpdate() {




    }

})