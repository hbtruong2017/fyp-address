<template>


  <div v-if="selectedCountries && countriesMetadata">

      <v-card class="mx-auto" outlined style="padding-bottom: 20px;">

          <!-- for loop: displays country name and flag image -->
          <div v-for="cname in selectedCountries" :key=cname>

              <v-row class="mx-auto">
                  <v-col class="mx-auto">
                      <div class="sidebarCountryName">{{ cname }}</div>
                  </v-col>
              </v-row>

              <v-row v-if="countriesMetadata[cname] && countriesMetadata[cname]['flag']">
                  <div class="countryFlagSidebarSection">
                      <img class="countryFlagSidebar" :src="countriesMetadata[cname]['flag']" aspect-ratio="2" contain/>
                  </div>
              </v-row>

          </div>

          <!-- Countries to compare button -->
          <v-row justify="center">

              <v-btn
                  color="#004D8E"
                  class="white--text mb-2 sidebar"
                  depressed
                  width="250"
                  @click=emitCountry>
                  Countries to Compare
              </v-btn>

          </v-row>



        <!-- download csv button -->
          <v-row justify="center" v-if="CSVData">

              <vue-json-to-csv :json-data="CSVData" :csv-title="'countries_data'">

                  <v-btn
                      outlined
                      color="#004D8E"
                      class="mb-2 sidebar"
                      width="250"
                      depressed>

                      <v-icon style="margin-right:5px">
                          mdi-download
                      </v-icon>

                      Download CSV
                  </v-btn>

            </vue-json-to-csv>

          </v-row>

      </v-card>

  </div>


</template>

<script>

import VueJsonToCsv from 'vue-json-to-csv'

export default {

  name: "metadata-panel",

  components: {
    "vue-json-to-csv": VueJsonToCsv
  },

  props: ["selectedCountries", "countriesMetadata", "CSVData"],

  methods: {

    emitCountry() {
      //this function is called when "countries to compare" button is clicked
      //this function emits an event to the parent component to handle
      this.$emit("selectCountriesButtonClicked")
    },


  }

}

</script>

<style>

.sidebarCountryName {
  color: #333333 !important;
  font-weight: 700;
  font-size: 22px;
  text-align: center;
}

.countryFlagSidebar {
  height: 48px;
  margin-bottom: 10px;
}

.countryFlagSidebarSection {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
}


</style>
