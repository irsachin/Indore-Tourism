import React from 'react'
import '../css/Slideshow.css'

const Slideshow = () => {
  return (
    <>
    <div className="slideshow">
        <div className="slides">
            <img src="https://picsum.photos/seed/picsum/200/300" alt="" className="slideshow-img" />
        </div>
        <div className="slides">
            <img src="https://picsum.photos/seed/picsum/200/300" alt="" className="slideshow-img" />
        </div>
        <div className="slides">
            <img src="https://picsum.photos/seed/picsum/200/300" alt="" className="slideshow-img" />
        </div>
    </div>
    </>
  )
}

export default Slideshow