<script>
    let content = '';
    $: isBad = content.includes("CS Cup 2023");

    function getContent(){
        chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
            const activeTab = tabs[0];

            if(activeTab){
                chrome.scripting.executeScript({
                    target: { tabId: activeTab.id },
                    function: () => {
                        return document.body.innerText
                    },
                }, (results) => {
                    if (results && results[0] && results[0].result) {
                        const documentElement = results[0].result;
                        content = documentElement;
                    } else {
                        console.log({ error: 'Failed to retrieve HTML' });
                    }
                });
            }
        });
    }
    getContent();
</script>

<main>
    <div>
        {#if isBad == true}
            <p id='bad-text'>SUSPECIOUS CONTENT DETECTED!</p>
        {:else}
            <p id='good-text'>Nothing Wrong</p>
        {/if}
    </div>
</main>

<style>
    *{
        padding: 0px;
        margin: 0px;
    }
    #bad-text{
        font-size: 1rem;
        color: white;
        background-color: red;
    }
    #good-text{
        font-size: 1rem;
        color: white;
        background-color: green;
    }
</style>
