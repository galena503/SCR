

  Vue.component('vc_dlist_4', {
    props: ['schedule'],
    template: `
    
    `
})

  Vue.component('vc_dlist_4', {
    props: ['schedule'],
    template: `
    <div
        v-for="schedule_d key in schedule"
    >
        <h3>[[ schedule.key ]]</h3>
        <table>
            <tr
                v-for="schedule_d in schedule.items"
            >
                <tb>[[schedule_d.f]]</tb>
                <tb>[[schedule_d.s]]</tb>
            </tr>
        </table>
    </div> 
    `
  })
