from app import app


@app.route('/')
def defaultpath():
    return "This domain is currently not working. Please try back later."


@app.route('/itattt/v1.0/maker/location/<string:person>/<string:event>/<string:location>')
@app.route('/itattt/v1.0/maker/location/<string:person>/<string:event>/<string:location>/<path:coordinates>')
def location_sms(person, event, location, coordinates=None):
    action = person + "_" + event + "_" + location

    location_update(person, event, location)

    key = getkeyforevent(action)

    if coordinates:
        r = re.search('q=(.*)&z=', coordinates)
        print r.group(1)
        globals()[action](action, key, r.group(1))
    else:
        globals()[action](action, key)

    # if key:
    #     sendtoifttt(action, key)
    #
    # else:
    #     print action, key
    #     printlocation()

    return "Something", 200


if __name__ == '__main__':
    app.run()
