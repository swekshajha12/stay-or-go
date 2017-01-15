from flask import render_template, request, jsonify
import feedparser

from stayorgo import app
from .bom_ftp import wx_obs, station_list
from .cfa_ftp import fetch_emv_tfb, fetch_emv_fdr
from .wun_ftp import fetch_wun_forecast

from datetime import datetime

@app.route('/') #, methods=['GET','POST'])
def stayorgo():
    # default page
    return render_template('index.html')


@app.route('/api/wx/current/<station_id>', methods=['POST'])
def api_wx_current(station_id):
    # fetch the current weather for a given weather station id.
    # ftp://ftp.bom.gov.au/anon/gen/fwo/IDV60920.xml
    if request.method == "POST":
        #wx = {}
        #wx['station_id'] = station_id

        obs = wx_obs("IDV60920", station_id)

        return jsonify(obs)


@app.route('/api/wx/forecast/<station_id>')
def api_wx_forecast(station_id):
    # fetch the current weather for a given weather station id.
    #
    wx = {}
    wx['station_id'] = station_id

    return jsonify(wx)


@app.route('/api/wu/forecast/<station_id>', methods=['POST','GET'])
def api_wu_forecast(station_id):
    # fetch the current wu weather for a given weather station id.
    #
    wx = fetch_wun_forecast(station_id)

    return jsonify(wx)


@app.route('/api/wx/station/<station_id>', methods=['POST','GET'])
def api_wx_station(station_id):
    # fetch the current weather for a given weather station id.
    #
    #wx = {}
    #wx['station_id'] = station_id
    wx = station_list(station_id)

    return jsonify(wx)


@app.route('/api/fx/forecast/fdr/<district>')
def api_fdi_forecast(district):
    # fetch the current official fdi forecast for the state
    #
    #fx = fetch_cfa_fdr_tfb("tfbfdrforecast_rss")
    # fx = fetch_emv_fdr_tfb("FDRTFBJSON")
    fx = fetch_emv_fdr("FDRTFBXML",district)

    #print(fx)
    return jsonify(fx)


@app.route('/api/fx/forecast/tfb/<district>')
def api_tfb_forecast(district):
    # fetch the current official fdi forecast for the state
    #
    #fx = fetch_cfa_fdr_tfb("tfbfdrforecast_rss")
    # fx = fetch_emv_fdr_tfb("FDRTFBJSON")
    fx = fetch_emv_tfb("FDRTFBXML",district)

    #print(fx)
    return jsonify(fx)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404