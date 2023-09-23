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
	<table class="styled-table">
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
				<td>#{row.id}</td>
				<td>{row.name}</td>
				<td>{row.description}</td>
				<td>{row.type}</td>
				<td><Time timestamp={row.created_at} /></td>
				<td>{row.lifespan_in_years} years</td>
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

	.list-title {
		margin-bottom: 15vh;
		color: #009879;
	}

	.styled-table {
		border-collapse: collapse;
		margin: 25px 0;
		font-size: 0.9em;
		font-family: sans-serif;
		min-width: 400px;
		box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
	}

	td {
		letter-spacing: 1px;
	}
	
	.styled-table thead tr {
		background-color: #009879;
		color: #ffffff;
		text-align: left;
	}
	
	tbody td {
		text-align: left;
		border-bottom: 1px solid black;
	}

	.styled-table th,
	.styled-table td {
		padding: 12px 15px;
	}

	.styled-table tbody tr {
    	border-bottom: 1px solid #dddddd;
	}

	.styled-table tbody tr:nth-of-type(even) {
		background-color: #f3f3f3;
	}

	.styled-table tbody tr:last-of-type {
		border-bottom: 2px solid #009879;
	}
</style>