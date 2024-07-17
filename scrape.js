// Settings
const { token, fetchChanel_id } = require("./settings.json");

// Modules
const { greenBright } = require("chalk");
const ora = require("ora");
const fs = require("fs");

const fetch = require("node-fetch");

// Start
Main();

/**
 * Request messages
 */
async function request(before) {
    try {
        const options = {
            method: "GET",
            headers: { authorization: token }
        };
        const spinner = ora("Sending 'GET' Request(s)").start();
        setTimeout(() => {
            spinner.stop();
        }, 1000);
        const request = await fetch(
            `https://discord.com/api/channels/${fetchChanel_id}/messages?limit=100&${before ? "before=" + before : ""}`,
            options
        );
        return await request.json();
    } catch (error) {
        console.error("An error occurred during the request:", error);
        throw error; 
        }
    }

async function go() {
    let page = await request();
    const spinner = ora("Fetching...").start();
    count = 0;
    while (page.length >= 50 && count < 1000) {
        page = await request(page[page.length - 1].id);
        spinner.succeed(greenBright(`Fetched ${page.length} messages`));
        const scraped = page.map((attach) => attach.attachments.map(url => url.proxy_url)).map((getlink) => getlink.toString()).filter(e => e);
        const currArr = scraped.map(l =>  l.split(',') ).flat();
        spinner.succeed(greenBright(`Extracted ${currArr.length} images | Check "links.jsonl"`));
        jlstrings = currArr.map(JSON.stringify).join('\n');
        fs.writeFileSync("links.jsonl", jlstrings, {flag:'a'});
        count += 1;
    }
}

function Main() {
    request().then(() => { go(); });
}
