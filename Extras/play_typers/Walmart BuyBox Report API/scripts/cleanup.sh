#!/bin/bash
cd "~/app/Walmart BuyBox Report API"
trap cleanup EXIT
function cleanup(){
    # gio trash ./assets/report.json
    # gio trash ./logfile/*.log
    if [[ -x /usr/bin/gio ]]; then
        gio trash ./assets/report.json
        gio trash ./reports/$(date +%Y)-*
        gio trash ./logfile/*.log
    else
        rm ./assets/report.json
        # rm -rf ./reports/$(date +%Y)-* not recoverable
        rm ./logfile/*.log
    fi
}