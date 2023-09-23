<script>
    import { onMount } from "svelte";
	import Time from "svelte-time";

	import { apiData, assetsList } from "../src/store.js"

	onMount(async () => {
		fetch("http://localhost:8000/assets")
		.then(response => response.json())
		.then(data => {
			console.log(data),
			apiData.set(data)
		}).catch(error => {
			console.log(error)
			return []
		})
	})

	let columns = ["ID", "Name", "Description", "Type", "Created at", "Lifespan"]
</script>

<main>
	<h1 class="list-title">Your Assets</h1>
	<table>
		<thead>
		<tr>
			{#each columns as column}
				<th>{column}</th>
			{/each}
		</tr>
		</thead>

		<tbody>
		{#each $assetsList as row}
			<tr>
				<td>{row.id}</td>
				<td>{row.name}</td>
				<td>{row.description}</td>
				<td>{row.type}</td>
				<td><Time timestamp={row.created_at} /></td>
				<td>{row.lifespan_in_years}</td>
			</tr>
		{/each}
		</tbody>
	</table>
</main>

<style>
	@import url("https://fonts.googleapis.com/css2?family=Montserrat&display=swap");

	table {
		table-layout: fixed;
		width: 100%;
		border-collapse: collapse;
		border: 1px solid black;
		border-radius: 5px;
	}

	th, td {
		padding: 20px;
	}

	.list-title {
		margin-bottom: 15vh;
	}

	th {
  		letter-spacing: 2px;
		background-color: #53a25c;
		color: #000000;
	}

	td {
		letter-spacing: 1px;
	}
	
	thead tr {
		border-bottom: 1px solid black;
	}
	
	tbody td {
		text-align: center;
		border-bottom: 1px solid black;
	}
</style>