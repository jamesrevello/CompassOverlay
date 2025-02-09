chrome.action.onClicked.addListener((tab) => {
    chrome.tabs.sendMessage(tab.id, { action: "toggleCompass" });
  });
  
  chrome.commands.onCommand.addListener((command, tab) => {
    if (command === "_execute_action") {
      chrome.tabs.sendMessage(tab.id, { action: "toggleCompass" });
    }
  });
  