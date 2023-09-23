<script>
    import { onMount } from "svelte";
	import  Chart  from  "../src/components/Chart.svelte";
	import  {  visits,  pages,  referrers,  os,  browsers,  devices  }  from  "./data.js";

	onMount(async () => {
		fetch("http://localhost:8000/assets")
		.then(response => response.json())
		.then(data => {
			console.log(data)
		}).catch(error => {
			console.log(error)
			return []
		})
	})
</script>

<main>
	<h3>Monthly Visitors</h3>
	
	<section>
		<Chart {...visits}/>
	</section>
	
	<h3>Top pages and Referrers</h3>
	<div id="pages">
		<section>
			<Chart {...pages}/>
		</section>
		<section>
			<Chart {...referrers}/>
		</section>
	</div>
	<h3>OS, Browsers and Devices</h3>
	<div id="devices">
		<section>
			<Chart {...os} showLegends={true}/>
		</section>
		<section>
			<Chart {...browsers} showLegends={true}/>
		</section>
		<section>
			<Chart {...devices} showLegends={true}/>
		</section>
	</div>
</main>

<style>
	@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");
  
	:global(*) {
	  margin: 0;
	  padding: 0;
	}
  
	:global(body) {
	  background-color: rgb(255, 137, 116);
	  font-family: "Montserrat", sans-serif;
	}
  
	main {
	  max-width: 800px;
	  min-height: 100vh;
	  margin: 0 auto;
	  padding: 0 20px;
	  background-color: rgb(245, 245, 245);
	}
  
	h3 {
	  padding: 20px 0;
	}
  
	section {
	  min-width: 100%;
	  background-color: white;
	  border-radius: 10px;
	}
  
	#pages {
	  display: grid;
	  grid-template-columns: repeat(2, 1fr);
	  gap: 20px;
	}
  
	#devices {
	  display: grid;
	  grid-template-columns: repeat(3, 1fr);
	  gap: 20px;
	  padding-bottom: 20px;
	}
  
	@media only screen and (max-width: 560px) {
	  #pages,
	  #devices {
		grid-template-columns: 1fr;
	  }
	}
  </style>