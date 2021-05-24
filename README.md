# Genshin Auto Daily Reward with Docker

## How to use

1. Install Docker
1. Run ``` sudo docker run -itd -e LTUID="yourLTUID" -e LTOKEN="yourLTOKEN" --name genshinadr kevincho9029/genshin-daily:1.1 ```
1. Register ```3 1 * * * docker start genshinadr``` in the system cron table. (```crontab -e```) If you haven't made docker available as a normal user, register it in the superuser cron table.(```sudo crontab -e```)
1. Finish!

## How to know my LTUID and LTOKEN?

[code based on ](https://arca.live/b/genshin/23930414)

## Dependency
[thesadru/genshinstats](https://github.com/thesadru/genshinstats)