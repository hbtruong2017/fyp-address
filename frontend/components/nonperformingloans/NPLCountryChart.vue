<template>
    <div v-if="chartData">    
        <v-row>
            <v-col v-for="chart in chartData":key=chart.title>
                <v-row>
                    <v-col>
                        <!-- title for each chart goes here -->
                        <div class="chartsTitle">
                            <h3>{{chart.title}}</h3>
                        </div>

                        <!-- each line-chart component goes here -->
                        <div class="charts" v-if="chart">
                            <line-chart :chartData=chart>
                            </line-chart>
                        </div>
                        <br>
                        <p class="chartsDescription">{{chart.description}}</p>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </div>
</template>

<script>

import LineChart from "@/components/analytics/lineChart.vue"

export default {

    name: "npl-country-chart",

    props: ["chartData"],

    components: {
        "line-chart": LineChart
    },

    data() {
        return {}
    },

}

</script>

<style>
    
.chartsTitle{
    color:#d29a42;
    margin-bottom:10px;
    text-align:center;
}

.chartsDescription {
    font-size:13px;
    padding-left:10px;
    padding-right:10px;
}

.charts {
    padding-left:10px;
    padding-right:10px;
}

</style>