import { writable, derived } from 'svelte/store';

/** Store for your data. 
This assumes the data you're pulling back will be an array.
If it's going to be an object, default this to an empty object.
**/
export const apiData = writable([]);

export const assetsList = derived(apiData, ($apiData) => {
  if ($apiData.assets){
    return $apiData.assets.map(asset => asset);
  }
  return [];
});