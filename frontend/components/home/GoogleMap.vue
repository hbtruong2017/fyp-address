<template>
  
  <div v-if="coordinates">

    <!-- Google map component starts here -->
    <GmapMap
      :options=gmapOptions
      :center=center
      :zoom="zoom"
      style="min-width: 100%; min-height: 500px;">

      <!-- google map marker goes here -->
      <div v-if="coordinates">
        
        <GmapMarker
          v-for="country in coordinates"
          :position="{lat: country.lat, lng: country.lon}"
          :key="country.name"/>

      </div>

    </GmapMap>

  </div>

</template>

<script>

export default {

  name: "GoogleMap",
  
  props: ["coordinates"],
  
  data() {
    return {

      gmapOptions: {
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false,
        disableDefaultUi: false
      },

    };
  },

  methods: {

  },


  computed: {

    center() {
      let lat = 0
      let lng = 0

      for (let i in this.coordinates) {
        let coordinate = this.coordinates[i]
        lat += coordinate.lat
        lng += coordinate.lon
      }

      return {lat:lat/this.coordinates.length, lng:lng/this.coordinates.length}

    },

    zoom() {
      if (this.coordinates.length==1 && this.coordinates[0].country == "Singapore") return 12
      if (this.coordinates.length == 1) return 6
      return 3
    },

  }
};
</script>

