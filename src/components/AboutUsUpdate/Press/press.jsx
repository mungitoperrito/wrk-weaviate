import React from 'react';
import styles from './styles.module.scss';
import { LinkButton } from '/src/theme/Buttons';
import Link from '@docusaurus/Link';
('/src/components/AboutUsUpdate/person');
import Person from '/src/components/AboutUsUpdate/person';
import people from '/static/data/people.json';
import { ButtonContainer } from '../../../theme/Buttons';

export default function Press() {
  return (
    <div className={styles.teamBG}>
      <div className="container" id="meet_the_team">
        <div className={styles.box}>
          <h1>Press</h1>
          <p className="text-center">
            Latest news, updates, and press releases.
          </p>
        </div>
        <div className={styles.parent}>
          <div className={styles.div1}>
            <div className={styles.sectionL}>
              <h3>Press release</h3>
              <p className={styles.pressText}>
                Weaviate Raises $50 Million Series B Funding to Meet Soaring
                Demand for AI Native Vector Database Technology
              </p>
              <p className={styles.date}>21 Apr, 2023</p>
            </div>
          </div>
          <div className={styles.div2}>
            <div className={styles.sectionR}>
              <h3>The Information</h3>
              <p className={styles.pressText}>
                Index Ventures Leads<br></br> $50 Million Investment<br></br> in
                AI Startup Weaviate
              </p>
              <p className={styles.date}>20 Apr, 2023</p>
            </div>
          </div>
          <div className={styles.div3}>
            <div className={styles.sectionB}>
              <h3>Tech Crunch</h3>
              <p className={styles.pressText}>
                Weaviate’ search engine opens up new ways to query your data
              </p>
              <p>
                Companies sit on a lot of unstructured data and often don’t have
                the capabilities to get much out of it. Now imagine having a way
                to store data and actually be able to ask it questions...
              </p>
              <p className={styles.date}>22 Feb, 2022</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
