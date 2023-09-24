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
    <div class="popup-container">
        {#if isBad == true}
            <p class="header"> Monas</p>
            <p id='bad-text'>SUSPICIOUS CONTENT DETECTED!</p>
        {:else}
            <p class="header"> Monas</p>
            <p id='good-text'>Nothing Wrong</p>
        {/if}
    </div>
</main>

<style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
  
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f0f0f0;
    }
  
    main {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 60vh;
    }
  
    .popup-container {
      text-align: center;
      padding: 20px;
      border-radius: 8px;
      background-color: #fff;
      border-radius: 20px;
      transition: transform 0.3s ease-in-out;
    }
  
    #bad-text {
      font-size: 1.5rem;
      color: #ff5252;
      background-color: #fff; 
      padding: 15px 30px;
      border-radius: 4px;
      margin-bottom: 20px;
    }
  
    #good-text {
      font-size: 1.5rem;
      color: #4caf50;;
      background-color: white;
      padding: 15px 30px;
      border-radius: 4px;
    }
  
    .popup-container:hover {
      transform: scale(1.05);
    }

    .header{
        padding-top: 10px;
        font-weight : bold ;
        font-family: 'JetBrains Mono', monospace;
        font-size: 2rem;
        color: blue;
    }
  </style>
  
  
