If your name isn't aaron-price, this won't work.

It's a helper cli for setting up a fresh centos vps for use with my own "Crucible" web framework, which is in a private repo

## Usage:
spinup a droplet


```bash 
yum install -y git && \
git clone https://github.com/aaron-price/crucible_cli.git && \
./crucible_cli/__main__.py
```


You now have a web app running at your public ip address.

## Crucible:
- My second homemade web framework, focused on performance, security, and dev experience
- Functional, immutable, beautiful.
- Sub-milisecond response times ( <3 elixir )
- Clojurescript frontend (with cljs' implementation of react, redux)
- SCSS + PostCSS + BEM + My own custom functional/atomic style system.
- Graph database with a GraphQL api running db side (single round-trip no matter how crazy/recursive/etc.)
- Flexible and easy user auth with email authentication and easy integration with stripe for paid accounts.
- Python cli for bootstrapping it on a fresh digitalocean droplet.
